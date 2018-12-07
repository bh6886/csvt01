<!DOCTYPE html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>{{title}}</title>
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.4/css/bootstrap.min.css">
<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="http://cdn.bootcss.com/jquery/1.11.2/jquery.min.js"></script>
<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="http://cdn.bootcss.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
</head>


<style>
iframe {width:500px;height:90px;}
 body{
    /*background: blue;*/
       background-repeat: no-repeat;
          background-size:100% 100%;
             background-attachment: fixed;
                background-image:url('http://pic.58pic.com/58pic/12/62/06/99t58PICgie.jpg')

   }
   .STYLE9 {
           color: #FFFFFF;
                   font-weight: bold;
                   }
                   </style>

<body>
<div class="container-fluid">
        <div class="row-fluid">
                        <div class="span12">
                                                <h1 align="center" class="STYLE9">淘淘搜ops部署验证平台 </h1>
                                                                        <h3 align="center" class="STYLE9">服务器时间:{{time.0}}</h3>
                                                                                                <div class="tabbable" id="tabs-320427">
                                                                                                                                <ul class="nav nav-tabs">
                                                                                                                                                                <li class="active">

                                                <a href="#panel-11"   data-toggle="tab"><strong>mold发布</strong></a>                               </li>
                                                                                        <li>
                                                                                                                                        <a href="#panel-12" data-toggle="tab"><strong>app发布</strong></a>                                 </li>
                                                                                                                                                                                <li>
                                                                                                                                                                                                                                <a href="#panel-13"   data-toggle="tab"><strong>eng发布</strong></a>                                     </li>
                                                                                                                                                                                                                                                                       
                                </ul>
                                                                <div class="tab-content">
                                                                                                        <div class="tab-pane active" id="panel-11">
                                                                                                                                                        <p>
                                                                                                                                                                                                               <span class="STYLE9">1.工程包传输：</span>
                                                                                                                                                                                                                                                               <p>
                                                                                                                                                                                                                                                                                                               
	<input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldcp.html','_blank')" value="mold包线上传输"/>

	<p> <span class="STYLE9">2.打autoconfig,就算没有，也要点击：</span> <p>
	    <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldauto.html','_blank')" value="mold包打autoconfig"/>
	        
    <p> <span class="STYLE9">3.mold发布、日志查看、回滚：</span> <p>
        
 <p>
  <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.12发布"/>
  	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.12日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.12回滚"/>
  	         <p>
  	             <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.13发布"/>
  	             	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.13日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	             	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.13回滚"/>
  	             	      <p>   
  	             	           <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.14发布"/>
  	             	           	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.14日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	             	           	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.14回滚"/>
  	             	           	      <p>   
  	             	           	          <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.24发布"/>
  	             	           	          	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.25日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	             	           	          	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.25回滚"/>
  	             	           	          	       <p>  
  	             	           	          	           <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.25发布"/>
  	             	           	          	           	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.25日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	             	           	          	           	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.25回滚"/>
  	             	           	          	           	       <p>  
  	             	           	          	           	           <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.29发布"/>
  	             	           	          	           	           	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.29日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	             	           	          	           	           	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.29回滚"/>
  	             	           	          	           	           	      <p>  
  	             	           	          	           	           	          <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.32发布"/>
  	             	           	          	           	           	          	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.32日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
  	             	           	          	           	           	          	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.32回滚"/>
  	             	           	          	           	           	          	        
      <p>  
          <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.181发布"/>
          	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.181日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
          	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.181回滚"/>
          	        
      <p>  
          <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="0.65发布"/>
          	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="0.65日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
          	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="0.65回滚"/>
          	        
      <p>  
          <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="0.8发布"/>
          	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="0.8日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
          	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="0.8回滚"/>
          	        
      <p>  
          <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.174发布"/>
          	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.174日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
          	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.174回滚"/>  <p>  
          	        
    <input class="btn btn-primary" name="button82" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldep_24.html','_blank')" value="3.175发布"/>
    	<input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldlog_24.html','_blank')" value="3.175日志查看"/>&nbsp;&nbsp;&nbsp;&nbsp;
    	    <input class="btn btn-primary" name="button72" type="button" class="STYLE1" onClick="window.open('http://192.168.3.31/moldhg_24.html','_blank')" value="3.175回滚"/>


<p class="STYLE5">&nbsp;</p>




                                                   
          <div class="btn-group" role="group" aria-label="...">                         </div>
                                                          </p>
                                                                         </div>
                                                                                  <div class="tab-pane" id="panel-12">
                                                                                                 <p>
                                                                                                                   <span class="STYLE9">广告比价的验证页面.</span>
                                                                                                                                                             <p>
                                                                                                                                                                                                                     <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/br.html','_blank')">br验证</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/recom.html','_blank')">recom验证</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/showmold.html','_blank')">广告mold验证</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/showapp.html','_blank')">广告app验证</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/showeng.html','_blank')">广告eng验证</button>
                                                                                                  </p>
                                                                                                                                          </div>
                                                                                                                                                                                  <div class="tab-pane" id="panel-13">
                                                                                                                                                                                                                                  <p>
                                                                                                                                                                                                                                                                                          <span class="STYLE9">主站各项目的发布页面.</span>
                                                                                                                                                                                                                                                                                                                                    <p>
                                                                                                                                                                                                                                                                                                                                                                                            <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs.html','_blank')">主站www发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-app.html','_blank')">主站app发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-client.html','_blank')">主站client发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-item.html','_blank')">主站item发布</button>
                                                                                                  <p>
                                                                                                                                                          <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-search.html','_blank')">主站search发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-service.html','_blank')">主站service发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-tejia.html','_blank')">主站tejia发布</button>
                                                                                                  
                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-tuan.html','_blank')">主站tuan发布</button>
                                                                                                  <p>
                                                                                                                                                          <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-sitemap.html','_blank')">主站sitemap发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-dapei.html','_blank')">主站dapei发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-back.html','_blank')">主站back发布</button>

                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-control.html','_blank')">主站control发布</button>
                                                                        
                                                        <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/zzbs-app99.html','_blank')">主站app.99发布</button>
                                                                                             
                                        </div>

                                </div>
                                                        </div>
                                                        <span class="STYLE9">4.广告统一验证页面的发布页面.</span> <p>
                                                        <p>
                                                         <button class="btn btn-primary " type="button" onClick="window.open('http://192.168.3.31/showmold.html','_blank')">广告各服务验证</button><br>
                                                         <p>
                                                         <script type="text/javascript">
                                                         (function() {
                                                         	var btn = $(".btn");
                                                         		btn.on("click", function(e) {
                                                         				var thisBtn = $(this);
                                                         						thisBtn.addClass("btn-success").data("stat", "true");
                                                         							});
                                                         							})()
                                                         							</script>
                                                         							                      
   

    <div align="left">
          <p><img alt="140x140" src="http://img.taotaosou.cn/image13/M06/13/03/wKgDslV6e5IIAAAAAAFD7v-MpJEAAdVWABIBfQAAUQG317.jpg" />      </p>
                <p>&nbsp;</p>
                      <p>&nbsp;</p>
                            <p>&nbsp;</p>
                                  <address> 
                                        <strong>博涵Dream.S</strong><br />
                                              bh6886@qq.com<br />  
                                                    <abbr title="Phone">P:</abbr> 13372542902
                                                          </address>
                                                          </div>
