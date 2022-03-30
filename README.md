# ECNU-dase-Laoze

   本仓库是华东师范大学数据学院老子项目的代码整合，主要分为两部分，一是老子前期数据的爬取和处理的代码整合，另一部分是基于springboot，mybaits等框架的老子项目web展示系统。在运行之前，您需要确保已安装并配置好如下环境：
  1. java 1.8
  2. mysql 5.7.36
  3. nodejs
  4. maven （可选）
  5. ideal （可选）
  
  ## laozi-vue
  
  基于前后端分离的理念，我们基于vue框架独立开发了前端页面。使用请命令行进入laozi-vue/vue-laozi目录下，输入命令：
  
  `npm install`
  
  来安装依赖。当然，该阶段耗时较长，且由于配置，版本，网络等这种不可知的原因导致bug安装出错，您也可以跳过这一步。下载项目目录下的*node_modules*目录，将该目录复制到laozi-vue/vue-laozi目录下即可。
  
  依赖安装完成之后，在laozi-vue/vue-laozi目录下输入命令：
  
  `npm run dev`
  
  即可开启前端。
  
 
 ## laozi
 
 首先，请确保老子的数据成功导入mysql数据库。请通过[百度云链接](https://pan.baidu.com/s/1m5Nrs92DVVElaXk0409hhw)下载laozi.sql数据库文件，提取码为本实验室两任老师的姓名首字母加上实验室房间号。使用命令：
 
 `mysql -u[用户名]    -p[密码]    <  [laozi.sql]`
 
 导入数据即可。
 
 
 基于前后端分离的理念，我们使用springboot,mybaits等工具开发了老子的后端。您可以使用ideal打开laozi目录，在左侧工程栏中找到porn.xml文件，在工程目录中右击该文件点击mark as mavean，即可正常使用maven管理该项目。使用maven安装好各项依赖后，运行*src/main/java/com/laozi/LaoziApplication*即可开启后端。
 此外，您可以通过*src/main/resources/application.yml*修改数据端口和用户名密码。
 
 另外，我们也通过[百度云](https://pan.baidu.com/s/1OSS7aitK21sV_9aE9KKVDw)提供了打包好的jar包，提取码为8419，您只需下载jar包，使用命令：
 `java -jar laozi-0.0.1-SNAPSHOT.jar`
 即可开启后端。
 
 至此，老子项目已经顺利开启，您只需要在浏览器中打开*http://localhost:8081/*即可访问页面
 
 
