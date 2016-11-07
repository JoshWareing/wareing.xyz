<!DOCTYPE html>
<html>
  <head>
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"bc12d0ca7c","applicationID":"1887052,5587075","transactionName":"IlgMRUFXWFhWEE5TUhVDB0NsXUZGXBA+QVYGUhEeQ0pRQloHFg==","queueTime":0,"applicationTime":7,"ttGuid":"","agentToken":null,"agent":"js-agent.newrelic.com/nr-632.min.js"}</script>
<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o?o:n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({QJf3ax:[function(e,n){function t(e){function n(n,t,a){e&&e(n,t,a),a||(a={});for(var u=c(n),f=u.length,s=i(a,o,r),p=0;f>p;p++)u[p].apply(s,t);return s}function a(e,n){f[e]=c(e).concat(n)}function c(e){return f[e]||[]}function u(){return t(n)}var f={};return{on:a,emit:n,create:u,listeners:c,_events:f}}function r(){return{}}var o="nr@context",i=e("gos");n.exports=t()},{gos:"7eSDFh"}],ee:[function(e,n){n.exports=e("QJf3ax")},{}],3:[function(e,n){function t(e){return function(){r(e,[(new Date).getTime()].concat(i(arguments)))}}var r=e("handle"),o=e(1),i=e(2);"undefined"==typeof window.newrelic&&(newrelic=window.NREUM);var a=["setPageViewName","addPageAction","setCustomAttribute","finished","addToTrace","inlineHit","noticeError"];o(a,function(e,n){window.NREUM[n]=t("api-"+n)}),n.exports=window.NREUM},{1:12,2:13,handle:"D5DuLP"}],"7eSDFh":[function(e,n){function t(e,n,t){if(r.call(e,n))return e[n];var o=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:o,writable:!0,enumerable:!1}),o}catch(i){}return e[n]=o,o}var r=Object.prototype.hasOwnProperty;n.exports=t},{}],gos:[function(e,n){n.exports=e("7eSDFh")},{}],handle:[function(e,n){n.exports=e("D5DuLP")},{}],D5DuLP:[function(e,n){function t(e,n,t){return r.listeners(e).length?r.emit(e,n,t):(o[e]||(o[e]=[]),void o[e].push(n))}var r=e("ee").create(),o={};n.exports=t,t.ee=r,r.q=o},{ee:"QJf3ax"}],id:[function(e,n){n.exports=e("XL7HBI")},{}],XL7HBI:[function(e,n){function t(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:i(e,o,function(){return r++})}var r=1,o="nr@id",i=e("gos");n.exports=t},{gos:"7eSDFh"}],G9z0Bl:[function(e,n){function t(){var e=d.info=NREUM.info,n=f.getElementsByTagName("script")[0];if(e&&e.licenseKey&&e.applicationID&&n){c(p,function(n,t){n in e||(e[n]=t)});var t="https"===s.split(":")[0]||e.sslForHttp;d.proto=t?"https://":"http://",a("mark",["onload",i()]);var r=f.createElement("script");r.src=d.proto+e.agent,n.parentNode.insertBefore(r,n)}}function r(){"complete"===f.readyState&&o()}function o(){a("mark",["domContent",i()])}function i(){return(new Date).getTime()}var a=e("handle"),c=e(1),u=(e(2),window),f=u.document,s=(""+location).split("?")[0],p={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-632.min.js"},d=n.exports={offset:i(),origin:s,features:{}};f.addEventListener?(f.addEventListener("DOMContentLoaded",o,!1),u.addEventListener("load",t,!1)):(f.attachEvent("onreadystatechange",r),u.attachEvent("onload",t)),a("mark",["firstbyte",i()])},{1:12,2:3,handle:"D5DuLP"}],loader:[function(e,n){n.exports=e("G9z0Bl")},{}],12:[function(e,n){function t(e,n){var t=[],o="",i=0;for(o in e)r.call(e,o)&&(t[i]=n(o,e[o]),i+=1);return t}var r=Object.prototype.hasOwnProperty;n.exports=t},{}],13:[function(e,n){function t(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(0>o?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=t},{}]},{},["G9z0Bl"]);</script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600" media="screen" rel="stylesheet" />
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" media="screen" rel="stylesheet" />


    <style>
      *{-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box}html,body,div,span,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,abbr,address,cite,code,del,dfn,em,img,ins,kbd,q,samp,small,strong,sub,sup,var,b,i,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,caption,article,aside,canvas,details,figcaption,figure,footer,header,hgroup,menu,nav,section,summary,time,mark,audio,video{margin:0;padding:0;border:0;outline:0;vertical-align:baseline;background:transparent}article,aside,details,figcaption,figure,footer,header,hgroup,nav,section{display:block}html{font-size:16px;line-height:24px;width:100%;height:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;overflow-y:scroll;overflow-x:hidden}img{vertical-align:middle;max-width:100%;height:auto;border:0;-ms-interpolation-mode:bicubic}body{min-height:100%;-webkit-font-smoothing:subpixel-antialiased}.clearfix{clear:both;zoom:1}.clearfix:before,.clearfix:after{content:&quot;\0020&quot;;display:block;height:0;visibility:hidden}.clearfix:after{clear:both}

    </style>
    <style>
  body.background.error-page-wrapper, .background.error-page-wrapper.preview {
    font-family: 'Source Sans Pro', sans-serif;
    background-position:center center;
    background-repeat:no-repeat;
    background-size:cover;
    position:relative;
  }

  .background.error-page-wrapper .content-container {
    border-radius: 6px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0,0,0,.2);
    padding:50px;
    background-color: #fff;
    width:100%;
    max-width:525px;
    position:absolute;
    left:50%;
    margin-left:-262px;
  }

  .background.error-page-wrapper .content-container.in {
    left:0px;
    opacity:1;
  }

  .background.error-page-wrapper .head-line {
    transition:color .2s linear;
    font-size:48px;
    line-height:60px;
    letter-spacing: -1px;
    margin-bottom: 5px;
    color:#ccc;
  }
  .background.error-page-wrapper .subheader {
    transition:color .2s linear;
    font-size:36px;
    line-height:46px;
    color:#333;
  }
  .background.error-page-wrapper .hr {
    height:1px;
    background-color: #ddd;
    width:60%;
    max-width:250px;
    margin:35px auto;
  }
  .background.error-page-wrapper .context {
    transition:color .2s linear;
    font-size:18px;
    line-height:27px;
    color:#bbb;
  }
  .background.error-page-wrapper .context p {
    margin:0;
  }
  .background.error-page-wrapper .context p:nth-child(n+2) {
    margin-top:16px;
  }
  .background.error-page-wrapper .buttons-container {
    margin-top: 35px;
    overflow: hidden;
  }
  .background.error-page-wrapper .buttons-container a {
    transition:text-indent .2s ease-out, color .2s linear, background-color .2s linear;
    text-indent: 0px;
    font-size:14px;
    text-transform: uppercase;
    text-decoration: none;
    color:#fff;
    background-color:#2ecc71;
    border-radius: 99px;
    padding:12px 0 13px;
    text-align: center;
    display:inline-block;
    overflow: hidden;
    position: relative;
    width:45%;
  }

  .background.error-page-wrapper .buttons-container .fa {
    transition:left .2s ease-out;
    position: absolute;
    left:-50px;
  }

  .background.error-page-wrapper .buttons-container a:hover {
    text-indent: 15px;
  }

  .background.error-page-wrapper .buttons-container a:nth-child(1) {
    float:left;
  }

  .background.error-page-wrapper .buttons-container a:nth-child(2) {
    float:right;
  }

  .background.error-page-wrapper .buttons-container .fa-home {
    font-size:18px;
    top:15px;
  }

  .background.error-page-wrapper .buttons-container a:hover .fa-home {
    left:10px;
  }

  .background.error-page-wrapper .buttons-container .fa-warning {
    font-size:16px;
    top:17px;
  }

  .background.error-page-wrapper .buttons-container a:hover .fa-warning {
    left:5px;
  }

  .background.error-page-wrapper .buttons-container .fa-power-off {
    font-size:16px;
    top:17px;
  }

  .background.error-page-wrapper .buttons-container a:hover .fa-power-off {
    left:9px;
  }


  .background.error-page-wrapper .buttons-container.single-button {
    text-align: center;
  }

  .background.error-page-wrapper .buttons-container.single-button a  {
    float:none !important;
  }

  @media screen and (max-width: 555px) {
    .background.error-page-wrapper {
      padding:30px 5%;
    }
    .background.error-page-wrapper .content-container {
      padding:37px;
      position: static;
      left: 0;
      margin-left:0;
    }
    .background.error-page-wrapper .head-line {
      font-size:36px;
    }
    .background.error-page-wrapper .subheader {
      font-size:27px;
      line-height: 37px;
    }
    .background.error-page-wrapper .hr {
      margin:30px auto;
      width:215px;
    }
    .background.error-page-wrapper .buttons-container .fa {
      display:none;
    }
    .background.error-page-wrapper .buttons-container a:hover {
      text-indent: 0px;
    }
  }

  @media screen and (max-width: 450px) {
    .background.error-page-wrapper {
      padding:30px;
    }
    .background.error-page-wrapper .head-line {
      font-size:32px;
    }
    .background.error-page-wrapper .hr {
      margin:25px auto;
      width:180px;
    }
    .background.error-page-wrapper .context {
      font-size:15px;
      line-height:22px;
    }

    .background.error-page-wrapper .context p:nth-child(n+2) {
      margin-top:10px;
    }
    .background.error-page-wrapper .buttons-container {
      margin-top:29px;
    }
    .background.error-page-wrapper .buttons-container a {
      float:none !important;
      width:65%;
      margin:0 auto;
      font-size:13px;
      padding:9px 0;
    }

    .background.error-page-wrapper .buttons-container a:nth-child(2) {
      margin-top:12px;
    }
  }
</style>
    <style>


    .background-image {
      background-color: #FFFFFF;
      background-image: url(https://qujxzg.bl3302.livefilestore.com/y2pB3F3OS6ZcWYQw8XvWtwNRchR0-KZuI8Um9y4aWXdLFyuF0mZk6bkayk9HW7Pw9JVmt3l-khQ6qqtVowlHuDiRg7DJTE6oRvxbTJTs_6LulAakjraQMBkhfA2wdnV23VelPaEyCiMDBPtX2BBjAd1VfDO564oRsSro-hM82OzuE0/bg.jpg) !important;
    }

    .primary-text-color {
      color: #494949 !important;
    }

    .secondary-text-color {
      color: #AAAAAA !important;
    }

    .sign-text-color {
      color: #FFBA00 !important;
    }

    .sign-frame-color {
      color: #343C3F;
    }

    .pane {
      background-color: #FFFFFF !important;
    }

    .border-button {
      color: rgba(59, 89, 153, 1) !important;
      border-color: rgba(59, 89, 153, 1) !important;
    }
    .button {
      background-color: rgba(59, 89, 153, 1) !important;
      color: #FFFFFF !important;
    }

    .shadow {
      box-shadow: 0 0 60px #000000;
    }

</style>
  </head>
  <body class="background error-page-wrapper background-color background-image">
    	
<div class="content-container shadow">
	<div class="head-line secondary-text-color">
		503
	</div>
	<div class="subheader primary-text-color">
		Looks like we're having some server issues.
	</div>
	<div class="hr"></div>
  <div class="context secondary-text-color">
    
    <p>
      Go back to the previous page and try again.
      If you think something is broken, report a problem.
    </p>


  </div>
	<div class="buttons-container single-button">
		<a class="button" href="mailto:https://www.joshuawareing.com/a/helpdesk" target="_blank"><span class="fa fa-warning"></span> Report A Problem</a>
	</div>
</div>

    <script>
      function ErrorPage(e,t,n){this.$container=$(e),this.$contentContainer=this.$container.find(n=="sign"?".sign-container":".content-container"),this.pageType=t,this.templateName=n}ErrorPage.prototype.centerContent=function(){var e=this.$container.outerHeight(),t=this.$contentContainer.outerHeight(),n=(e-t)/2,r=this.templateName=="sign"?-100:0;this.$contentContainer.css("top",n+r)},ErrorPage.prototype.initialize=function(){var e=this;this.centerContent(),this.$container.on("resize",function(t){t.preventDefault(),t.stopPropagation(),e.centerContent()}),this.templateName=="plain"&&window.setTimeout(function(){e.$contentContainer.addClass("in")},500),this.templateName=="sign"&&$(".sign-container").animate({textIndent:0},{step:function(e){$(this).css({transform:"rotate("+e+"deg)","transform-origin":"top center"})},duration:1e3,easing:"easeOutBounce"})},ErrorPage.prototype.createTimeRangeTag=function(e,t){return"<time utime="+e+' simple_format="MMM DD, YYYY HH:mm">'+e+"</time> - <time utime="+t+' simple_format="MMM DD, YYYY HH:mm">'+t+"</time>."},ErrorPage.prototype.handleStatusFetchSuccess=function(e,t){if(e=="503")$("#replace-with-fetched-data").html(t.status.description);else if(!t.scheduled_maintenances.length)$("#replace-with-fetched-data").html("<em>(there are no active scheduled maintenances)</em>");else{var n=t.scheduled_maintenances[0];$("#replace-with-fetched-data").html(this.createTimeRangeTag(n.scheduled_for,n.scheduled_until)),$.fn.localizeTime()}},ErrorPage.prototype.handleStatusFetchFail=function(e){$("#replace-with-fetched-data").html("<em>(enter a valid StatusPage.io url)</em>")},ErrorPage.prototype.fetchStatus=function(e,t){if(!e||!t||t=="404")return;var n="",r=this;t=="503"?n=e+"/api/v2/status.json":n=e+"/api/v2/scheduled-maintenances/active.json",$.ajax({type:"GET",url:n}).success(function(e,n){r.handleStatusFetchSuccess(t,e)}).fail(function(e,n){r.handleStatusFetchFail(t)})};
      var ep = new ErrorPage('body', "503", "background");
      ep.initialize();

      // hack to make sure content stays centered >_<
      $(window).on('resize', function() {
        $('body').trigger('resize')
      });

    </script>

    
  </body>
</html>
