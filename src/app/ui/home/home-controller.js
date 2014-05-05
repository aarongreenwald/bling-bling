bling.home.controller('HomeCtrl', ['$scope', '$http', function($scope, $http){
    $scope.home = new function(){
        var private = {
            saveWorklog: function(){
                $http({method: 'POST', url: 'api/worklog', data: {worklog: public.worklog}})
            }
        }
        
        var public = {          
            saveWorklog: private.saveWorklog,
            worklog: {
                workDate: '2014-05-07',
                taskId: null,
                timeSpent: null,
                note: null,
                isBillable: false
            }
        }
        
        return public
    }
}])
