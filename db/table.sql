CREATE TABLE client(client_id serial primary key not null
			,name varchar(50) NOT NULL
			,code varchar(8) NOT NULL
			--in the future I'll add billing info and other details here
			);

--this table represents one line item on an invoice for task-based billing. Does not yet support hourly billing
CREATE TABLE task (task_id serial primary key not null 
			,client_id int NOT NULL REFERENCES client
			,name varchar(50) NOT NULL
			,note text NULL
			,estimated_time decimal(12,2) NOT NULL --unit will be hours
			,invoice_amount decimal(19,4) NOT NULL
			,approved_date date NULL
			,completed_date date NULL --work completed, ready for invoicing.
			,paid_date date NULL --date payment is received. if payment is made in installments? This should really be in a separate table for remittances, with a M:M relationship to this table
			,paid_amount decimal(19,4) NULL
			,write_off_amount decimal(19,4) NULL
			,closed_date date NULL --means I can forget about this item
			--it cannot be closed until it's either paid or written off
			CHECK (paid_amount + write_off_amount = invoice_amount OR closed_date IS NULL)
			);

--an item here should represent one sitting of work
CREATE TABLE worklog(worklog_id serial primary key not null
			,work_date date NOT NULL
			,task_id int NOT NULL REFERENCES task
			--perhaps I'd rather track the start time and end time? I think this is more straightforward to compare to estimated time, and 
			--a record in this table might contain interrupted amounts, so this is better.
			,time_spent decimal(12,2) NOT NULL 	
			,note text NULL
			,is_billable boolean NOT NULL --even on project-based billing, useful for reporting
			);
