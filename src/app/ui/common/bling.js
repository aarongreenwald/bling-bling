var bling = angular.module('bling', [
    'ui.router'
    ])
     
bling.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/");

  $stateProvider
    .state('home', {
      url: "/",
      templateUrl: "home/home.html"
    })
})


