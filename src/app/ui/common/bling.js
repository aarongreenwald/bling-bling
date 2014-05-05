var bling = angular.module('bling', [
    'ui.router',
    'bling.home'
    ])
     
bling.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/");

  $stateProvider
    .state('home', {
      url: "/",
      templateUrl: "home/home.html"      
    })
})

bling.home = angular.module('bling.home', [])
