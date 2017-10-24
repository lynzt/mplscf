# coding=utf-8
def get_html():
    return r'''
    <!DOCTYPE HTML>
    <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
    <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
    <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
    <!--[if gt IE 8]><!-->
    <html  lang="en"> <!--<![endif]-->

    <head>

    <title>Campaign Finance Reporting System * version 2.2</title>

    	<meta charset="utf-8">
    	<meta name="robots" content="noindex">

    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    	<meta name="description" content="">


        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />


         <link href="assets/css/bootstrap.min.css" rel="stylesheet">
         <link href="assets/css/bootstrap.min.css" rel="stylesheet">
         <link rel="stylesheet"  href="assets/css/normalize.css">
         <link rel="stylesheet"  href="assets/css/main.css">
         <link rel="stylesheet" href="assets/css/docs.min.css">

         <!-- link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/responsive/1.0.0/css/dataTables.responsive.css"-->
         <link href="assets/css/bootstrap-table.css" rel="stylesheet">


       <link rel="stylesheet" href="http://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
       <script src="http://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>


       <script src="assets/js/vendor/modernizr-2.6.2-respond-1.1.0.min.js"></script>
       <script src="assets/js/jquery-1.11.3.min.js"></script>

       <script src="assets/js/bootstrap.min.js"></script>
       <script src="assets/js/bootstrap-table.js"></script>
       <!--script type="text/javascript" language="javascript" src="http://cdn.datatables.net/responsive/1.0.0/js/dataTables.responsive.min.js"></script-->




    </head>


    <body style="color:black">

    <div class="page-wrapper">
    <!-- header.jsp start -->




    	<div class="main-nav" name="navigation" role="navigation">
    		<nav class="page-nav">
    			<ul class="main-nav-item">

    			<li><a href="http://www.hennepin.us/"><span class="desktop icon-logo"></span>Home</a></li>
    			<li><a class="main-nav-item__handle" href="http://www.hennepin.us/residents"><span class="desktop icon-residents"></span>Residents</a>
    				<p class="desktop">Information and services</p>
    		    </li>
    		    <li>
    		    	<a class="main-nav-item__handle" href="http://www.hennepin.us/business"><span class="desktop icon-business"></span>Business</a>
    		        <p class="desktop">Regulations and opportunities</p>
    		    </li>
    		    <li>
    		    	<a class="main-nav-item__handle two-line" href="http://www.hennepin.us/your-government"><span class="desktop icon-your-government"></span>Your government</a>
    		        <p class="desktop">Leadership and engagement</p>
    		    </li>
    		    <li>
    		    	<a class="main-nav-item__handle two-line" href="http://www.hennepin.us/services"><span class="desktop icon-online-services"></span>Online services</a>
    		        <p class="desktop">Transactions and applications</p>
    		    </li>
    		</ul>
    		</nav>
    		<div class="topbar">
    			<nav class="topbar__nav">
    				<ul>
    					<li><a href="https://public.govdelivery.com/accounts/MNHENNE/subscriber/new " target="new">Subscribe</a></li>
    					<li><a href="http://www.hennepin.us/jobs">Jobs</a></li>
    					<li><a href="http://www.hennepin.us/employees">Employees</a></li>
    					<li><a href="http://www.hennepin.us/media">Media</a></li>
    					<li><a href="http://www.hennepin.us/contact/contact-information">Contact</a></li>


    				</ul>
    			</nav>
    		</div>
    	</div>

    <!-- header.jsp end -->
    <header class="site-header">
    	<a class="popout-nav--trigger" href="#navigation">Navigation</a>
    	<h1 class="site-title">Hennepin County, MN</h1>
    		</header>

    	<section class="page" >
    		<div class="content-wrapper">
    			<div class="container-fluid">








     <script src="assets/js/bootstrap-table-cookie.js"></script>



    <script>

    var delete_cookie = function(name) {
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    };

     function currencySorter(a, b) {
     		a = parseFloat(a.replace(/,/g,"").substring(1)); // remove $
            b = parseFloat(b.replace(/,/g,"").substring(1));        if (a > b) return 1;
            if (a < b) return -1;
            return 0;
        }

     function shortdateSorter(a, b) {
     		if(a.trim()=='') return 1;
     		if (b.trim()=='') return -1;
            a = Date.parse(a);
            b = Date.parse(b);
            if (a > b)  return 1;
            if (a < b) return -1;
            return 0;
        }


    function sub(){
    	frm = document.forms[0];
    	frm.action="getreports.do"
    	frm.submit();
    	}
    function sub1(parm){

    	frm = document.forms[0];
    	if(parm!=''){
        	frm.alpha.value=parm;
        }
        frm.method="post";
    	frm.action="search.do"
    	frm.submit();
    	}
    </script>

    <!-- begin Breadcrumbs  -->
    <div>
    <p><a href="http://www.hennepin.us/">Home</a>&gt;
    <a href="search_options.do">Campaign finance</a> &gt;Candidate
     </p></div>
    <!-- end Breadcrumbs  -->

    <div>
    <br />
            <p class="lead" style="line-height: 20px" >Candidate search results
            <br>
            <span style="font-size:0.7em"><br/>To narrow the results, click on a number or letter to jump to that section. Click on a candidate's name to view submitted documents.</span>
            </p>
    </div>

    <form name="searchForm" method="post" action="/cfrs/search.do">







      <div class="table-responsive">
      <div style="float:left;">
     		<label style="float: left">Filter by:
    	     <select name="filterBy" onchange="javascript:sub1('');" style="width:25%;display:inline"><option value="">&nbsp;</option>
    	     <option value="showall">Show all</option>
    	     <option value="active" selected="selected">Active only</option>
    	     <option value="terminated">Terminated only</option></select>
           </label>
         </div>
     <div  style="float:right;" >
            <h5>
            <label class="text-right">

    	           		 Results 1 to 181 of 181

    	              Show <a href="#" onclick="javascript:document.location.href ='search.do?searchBy=candidate&ps=10&pn=0&alpha=&filterBy=active&city=&office=&district='"> 10 </a> |
    	                   <a href="#" onclick="javascript:document.location.href ='search.do?searchBy=candidate&ps=25&pn=0&alpha=&filterBy=active&city=&office=&district='"> 25 </a> |
    	                   <a href="#" onclick="javascript:document.location.href ='search.do?searchBy=candidate&ps=181&pn=0&alpha=&filterBy=active&city=&office=&district='"> All </a>

    	   </label>





              <p id ="nav_panel" class="text-right">
    		     |<A onclick="javascript:sub1('0')" href="#" >0</A>
    		     |<A onclick="javascript:sub1('1')" href="#" >1</A>
    		     |<A onclick="javascript:sub1('2')" href="#" >2</A>
    		     |<A onclick="javascript:sub1('3')" href="#" >3</A>
    		     |<A onclick="javascript:sub1('4')" href="#" >4</A>
    		     |<A onclick="javascript:sub1('5')" href="#" >5</A>
    		     |<A onclick="javascript:sub1('6')" href="#" >6</A>
    		     |<A onclick="javascript:sub1('7')" href="#" >7</A>
    		     |<A onclick="javascript:sub1('8')" href="#" >8</A>
    		     |<A onclick="javascript:sub1('9')" href="#" >9</A>

    		     |<A href="#" onclick="javascript:sub1('A');">A</A>
    		     |<A href="#" onclick="javascript:sub1('B');">B</A>
    		     |<A href="#" onclick="javascript:sub1('C');">C</A>
    		     |<A href="#" onclick="javascript:sub1('D');">D</A>
    		     |<A href="#" onclick="javascript:sub1('E');">E</A>
    		     |<A href="#" onclick="javascript:sub1('F');">F</A>
    		     |<A href="#" onclick="javascript:sub1('G');">G</A>
    		     |<A href="#" onclick="javascript:sub1('H');">H</A>
    		     |<A href="#" onclick="javascript:sub1('I');">I</A>
    		     |<A href="#" onclick="javascript:sub1('J');">J</A>
    		     |<A href="#" onclick="javascript:sub1('K');">K</A>
    		     |<A href="#" onclick="javascript:sub1('L');">L</A>
    		     |<A href="#" onclick="javascript:sub1('M');">M</A>
    		     |<A href="#" onclick="javascript:sub1('N');">N</A>
    		     |<A href="#" onclick="javascript:sub1('O');">O</A>
    		     |<A href="#" onclick="javascript:sub1('P');">P</A>
    		     |<A href="#" onclick="javascript:sub1('Q');">Q</A>
    		     |<A href="#" onclick="javascript:sub1('R');">R</A>
    		     |<A href="#" onclick="javascript:sub1('S');">S</A>
    		     |<A href="#" onclick="javascript:sub1('T');">T</A>
    		     |<A href="#" onclick="javascript:sub1('U');">U</A>
    		     |<A href="#" onclick="javascript:sub1('V');">V</A>
    		     |<A href="#" onclick="javascript:sub1('W');">W</A>
    		     |<A href="#" onclick="javascript:sub1('X');">X</A>
    		     |<A href="#" onclick="javascript:sub1('Y');">Y</A>
    		     |<A href="#" onclick="javascript:sub1('Z');">Z</A>&nbsp;
    		  </p>

            </h5>
            </div>

            <table id="table" class="table table-striped table-hover table-condensed" style="padding: 1px;" cellspacing="1px"
            data-cookie="true"
            data-cookie-id-table="saveCommitteSort"
            data-show-toggle="true"
            data-toggle="table" >

                   <thead><tr>

                    <th data-field="candidate_name" data-align="left" data-sortable="true"><strong>Candidate name</strong></th>

                    <th data-field="committe_name" data-align="left" data-sortable="true"><strong>Committee name</strong></th>
                    <th data-field="regdate" data-align="left" data-sortable="true" data-sorter="shortdateSorter"><strong>Registration date</strong></th>
                    <th data-field="termdate" data-align="left" data-sortable="true" data-sorter="shortdateSorter"><strong>Termination date</strong></th>

                    <th data-field="location" data-align="left" data-sortable="true"><strong>Location</strong></th>
                    <th data-field="office" data-align="left" data-sortable="true"><strong>Office</strong></th>
                    <th data-field="district" data-align="left" data-sortable="true"><strong>District #</strong></th>

                    <th  data-field="revenues" data-align="left" data-sortable="true" data-sorter="currencySorter"><strong>YTD revenues</strong></th>
                    <th  data-field="expenses" data-align="left" data-sortable="true" data-sorter="currencySorter"><strong>YTD expenses</strong></th>
                    <th  data-field="cash_balance" data-align="left" data-sortable="true" data-sorter="currencySorter"><strong>Cash balance</strong></th>
                    </tr>
                  </thead>
                <tbody>





                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Adams, Justin';
                    					document.getElementById('ids').value='909';
                    					sub();
                    					">
                    Adams, Justin
                    </a>

                    </td>
                    <td align="left" valign="top">The Committee to Elect Justin C. Adams</td>

                    <td align="left" valign="top">

                    01/05/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Ali, Siad';
                    					document.getElementById('ids').value='834';
                    					sub();
                    					">
                    Ali, Siad
                    </a>

                    </td>
                    <td align="left" valign="top">Siad Ali for Minneapolis School Board</td>

                    <td align="left" valign="top">

                    12/27/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$734.33 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Anderson, Charlotte';
                    					document.getElementById('ids').value='85';
                    					sub();
                    					">
                    Anderson, Charlotte
                    </a>

                    </td>
                    <td align="left" valign="top">Charlotte Anderson for Library Board</td>

                    <td align="left" valign="top">

                    07/28/1989


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Library Board</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$81.33 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Arneson, Jenny';
                    					document.getElementById('ids').value='674';
                    					sub();
                    					">
                    Arneson, Jenny
                    </a>

                    </td>
                    <td align="left" valign="top">Jenny Arneson for School Board</td>

                    <td align="left" valign="top">

                    11/23/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,601.06 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Arulfo, Michael';
                    					document.getElementById('ids').value='931';
                    					sub();
                    					">
                    Arulfo, Michael
                    </a>

                    </td>
                    <td align="left" valign="top">Mike for Bloomington</td>

                    <td align="left" valign="top">

                    03/10/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$6,056.00</td>
                    <td align="left" valign="top" >$6,039.92</td>
                    <td align="left" valign="top" >$16.08 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Asberry, Tracine';
                    					document.getElementById('ids').value='710';
                    					sub();
                    					">
                    Asberry, Tracine
                    </a>

                    </td>
                    <td align="left" valign="top">Tracine Asberry for Minneapolis School Board</td>

                    <td align="left" valign="top">

                    03/05/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$313.43 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Axtell, Rod';
                    					document.getElementById('ids').value='502';
                    					sub();
                    					">
                    Axtell, Rod
                    </a>

                    </td>
                    <td align="left" valign="top">Axtell Volunteer Committee</td>

                    <td align="left" valign="top">

                    09/22/2005


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$2,452.56 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Baloga, Jack';
                    					document.getElementById('ids').value='702';
                    					sub();
                    					">
                    Baloga, Jack
                    </a>

                    </td>
                    <td align="left" valign="top">Baloga for Council Committee</td>

                    <td align="left" valign="top">

                    09/02/2011


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$50.17</td>
                    <td align="left" valign="top" >$50.00</td>
                    <td align="left" valign="top" >$3,445.99 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Becker, Carol';
                    					document.getElementById('ids').value='438';
                    					sub();
                    					">
                    Becker, Carol
                    </a>

                    </td>
                    <td align="left" valign="top">Becker Volunteer Committee</td>

                    <td align="left" valign="top">

                    03/11/2005


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Estimate &amp; Tax Board</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$1,150.00</td>
                    <td align="left" valign="top" >$1,569.06</td>
                    <td align="left" valign="top" >$1,422.86 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Bender, Lisa';
                    					document.getElementById('ids').value='750';
                    					sub();
                    					">
                    Bender, Lisa
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Lisa Bender</td>

                    <td align="left" valign="top">

                    12/13/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >10</td>
                    <td align="left" valign="top" >$31,955.00</td>
                    <td align="left" valign="top" >$47,517.24</td>
                    <td align="left" valign="top" >$50,799.35 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Bennett, Alicia';
                    					document.getElementById('ids').value='803';
                    					sub();
                    					">
                    Bennett, Alicia
                    </a>

                    </td>
                    <td align="left" valign="top">Alicia K Bennett for Mayor</td>

                    <td align="left" valign="top">

                    08/26/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$564.94 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Bicott, Zavier';
                    					document.getElementById('ids').value='785';
                    					sub();
                    					">
                    Bicott, Zavier
                    </a>

                    </td>
                    <td align="left" valign="top">Friends of Zavier Bicott</td>

                    <td align="left" valign="top">

                    06/17/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$230.70 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Bildsoe, Tim';
                    					document.getElementById('ids').value='949';
                    					sub();
                    					">
                    Bildsoe, Tim
                    </a>

                    </td>
                    <td align="left" valign="top">Tim for Ward 3</td>

                    <td align="left" valign="top">

                    06/27/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$3,450.00</td>
                    <td align="left" valign="top" >$304.02</td>
                    <td align="left" valign="top" >$3,145.98 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Bourn, Brad';
                    					document.getElementById('ids').value='621';
                    					sub();
                    					">
                    Bourn, Brad
                    </a>

                    </td>
                    <td align="left" valign="top">Brad Bourn for Parks</td>

                    <td align="left" valign="top">

                    04/17/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$9,473.84</td>
                    <td align="left" valign="top" >$6,537.27</td>
                    <td align="left" valign="top" >$12,641.73 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Brogan, Kris';
                    					document.getElementById('ids').value='103';
                    					sub();
                    					">
                    Brogan, Kris
                    </a>

                    </td>
                    <td align="left" valign="top">Citizens for Kris Brogan (Ward 13)</td>

                    <td align="left" valign="top">

                    03/04/1993


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >13</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$3.63 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Buckner, Brett';
                    					document.getElementById('ids').value='739';
                    					sub();
                    					">
                    Buckner, Brett
                    </a>

                    </td>
                    <td align="left" valign="top">Northside for Buckner</td>

                    <td align="left" valign="top">

                    09/12/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$8,100.75 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Bullard, Harrison';
                    					document.getElementById('ids').value='975';
                    					sub();
                    					">
                    Bullard, Harrison
                    </a>

                    </td>
                    <td align="left" valign="top">Bullard 4 Ward 12</td>

                    <td align="left" valign="top">

                    09/05/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >12</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Busse, Tim';
                    					document.getElementById('ids').value='699';
                    					sub();
                    					">
                    Busse, Tim
                    </a>

                    </td>
                    <td align="left" valign="top">Busse for Bloomington Committee</td>

                    <td align="left" valign="top">

                    07/07/2011


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >At Large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$369.60 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Callison, Jan';
                    					document.getElementById('ids').value='576';
                    					sub();
                    					">
                    Callison, Jan
                    </a>

                    </td>
                    <td align="left" valign="top">Callison Volunteer Committee</td>

                    <td align="left" valign="top">

                    03/24/2008


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$13,548.51 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Cano, Alondra';
                    					document.getElementById('ids').value='756';
                    					sub();
                    					">
                    Cano, Alondra
                    </a>

                    </td>
                    <td align="left" valign="top">People for Alondra</td>

                    <td align="left" valign="top">

                    01/06/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >9</td>
                    <td align="left" valign="top" >$14,910.00</td>
                    <td align="left" valign="top" >$22,385.32</td>
                    <td align="left" valign="top" >$6,816.60 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Caprini, Kimberly';
                    					document.getElementById('ids').value='869';
                    					sub();
                    					">
                    Caprini, Kimberly
                    </a>

                    </td>
                    <td align="left" valign="top">Kimberly Caprini for District 2 School Board Member</td>

                    <td align="left" valign="top">

                    02/10/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$341.07 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Carey, Jim';
                    					document.getElementById('ids').value='253';
                    					sub();
                    					">
                    Carey, Jim
                    </a>

                    </td>
                    <td align="left" valign="top">Jim Carey Volunteer Committee</td>

                    <td align="left" valign="top">

                    11/23/1992


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Three Rivers Park District</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$226.48 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Carlson, Robert (Andrew)';
                    					document.getElementById('ids').value='777';
                    					sub();
                    					">
                    Carlson, Robert (Andrew)
                    </a>

                    </td>
                    <td align="left" valign="top">Carlson for City Council</td>

                    <td align="left" valign="top">

                    05/03/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$22.17 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Carney Jr., Bob \'again\'';
                    					document.getElementById('ids').value='938';
                    					sub();
                    					">
                    Carney Jr., Bob &quot;again&quot;
                    </a>

                    </td>
                    <td align="left" valign="top">Bobagain for Mayor</td>

                    <td align="left" valign="top">

                    04/13/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$20.00</td>
                    <td align="left" valign="top" >$20.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Chamblis, Reva';
                    					document.getElementById('ids').value='780';
                    					sub();
                    					">
                    Chamblis, Reva
                    </a>

                    </td>
                    <td align="left" valign="top">Reva Chamblis Campaign Committee</td>

                    <td align="left" valign="top">

                    05/20/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Brooklyn Park</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >East</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$2,084.89 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Cobia, Jeffrey';
                    					document.getElementById('ids').value='649';
                    					sub();
                    					">
                    Cobia, Jeffrey
                    </a>

                    </td>
                    <td align="left" valign="top">Cobia for City Council</td>

                    <td align="left" valign="top">

                    08/19/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$718.91 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Colby, Jeanette';
                    					document.getElementById('ids').value='912';
                    					sub();
                    					">
                    Colby, Jeanette
                    </a>

                    </td>
                    <td align="left" valign="top">Friends of Jeanette</td>

                    <td align="left" valign="top">

                    01/11/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$14,093.00</td>
                    <td align="left" valign="top" >$7,680.97</td>
                    <td align="left" valign="top" >$6,412.03 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Colvin Roy, Sandra';
                    					document.getElementById('ids').value='73';
                    					sub();
                    					">
                    Colvin Roy, Sandra
                    </a>

                    </td>
                    <td align="left" valign="top">Colvin Roy for City Council (Ward 12)</td>

                    <td align="left" valign="top">

                    01/09/1997


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >12</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$3,907.64 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Coulter, Nathan';
                    					document.getElementById('ids').value='926';
                    					sub();
                    					">
                    Coulter, Nathan
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Nathan</td>

                    <td align="left" valign="top">

                    03/01/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$8,406.00</td>
                    <td align="left" valign="top" >$3,399.13</td>
                    <td align="left" valign="top" >$5,006.87 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Cowgill, Jono';
                    					document.getElementById('ids').value='933';
                    					sub();
                    					">
                    Cowgill, Jono
                    </a>

                    </td>
                    <td align="left" valign="top">Jono 4 Parks</td>

                    <td align="left" valign="top">

                    03/21/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$3,546.21</td>
                    <td align="left" valign="top" >$2,884.19</td>
                    <td align="left" valign="top" >$662.02 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Cunningham, Phillipe';
                    					document.getElementById('ids').value='895';
                    					sub();
                    					">
                    Cunningham, Phillipe
                    </a>

                    </td>
                    <td align="left" valign="top">Northside Neighbors for Cunningham</td>

                    <td align="left" valign="top">

                    11/28/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$20,232.40</td>
                    <td align="left" valign="top" >$21,592.33</td>
                    <td align="left" valign="top" >$1,520.61 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Dehn, Raymond';
                    					document.getElementById('ids').value='907';
                    					sub();
                    					">
                    Dehn, Raymond
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors United for Raymond Dehn</td>

                    <td align="left" valign="top">

                    12/30/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$54,702.10</td>
                    <td align="left" valign="top" >$40,814.62</td>
                    <td align="left" valign="top" >$19,766.07 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='DeJournett, Jennifer';
                    					document.getElementById('ids').value='738';
                    					sub();
                    					">
                    DeJournett, Jennifer
                    </a>

                    </td>
                    <td align="left" valign="top">Friends of Jennifer DeJournett</td>

                    <td align="left" valign="top">

                    08/29/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Three Rivers Park District</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$296.30 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Derus, Michael';
                    					document.getElementById('ids').value='887';
                    					sub();
                    					">
                    Derus, Michael
                    </a>

                    </td>
                    <td align="left" valign="top">Derus for Parks Committee</td>

                    <td align="left" valign="top">

                    06/22/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$1,385.94</td>
                    <td align="left" valign="top" >$4,434.99</td>
                    <td align="left" valign="top" >$5,218.34 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Eberhardy, Todd J.';
                    					document.getElementById('ids').value='662';
                    					sub();
                    					">
                    Eberhardy, Todd J.
                    </a>

                    </td>
                    <td align="left" valign="top">Eberhardy for Ward 9</td>

                    <td align="left" valign="top">

                    09/09/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >9</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$225.54 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Ellison, Jeremiah';
                    					document.getElementById('ids').value='899';
                    					sub();
                    					">
                    Ellison, Jeremiah
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Jeremiah</td>

                    <td align="left" valign="top">

                    12/02/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$9,854.78</td>
                    <td align="left" valign="top" >$11,999.59</td>
                    <td align="left" valign="top" >$3,164.37 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Ellison, Kim';
                    					document.getElementById('ids').value='718';
                    					sub();
                    					">
                    Ellison, Kim
                    </a>

                    </td>
                    <td align="left" valign="top">Kim Ellison for Students</td>

                    <td align="left" valign="top">

                    05/24/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$3,064.20 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Erickson, Joseph A.';
                    					document.getElementById('ids').value='217';
                    					sub();
                    					">
                    Erickson, Joseph A.
                    </a>

                    </td>
                    <td align="left" valign="top">Joseph Erickson Volunteer Committee (School Bd)</td>

                    <td align="left" valign="top">

                    06/08/2001


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$209.98 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Erwin, John';
                    					document.getElementById('ids').value='222';
                    					sub();
                    					">
                    Erwin, John
                    </a>

                    </td>
                    <td align="left" valign="top">Erwin for Park Board (At Large)</td>

                    <td align="left" valign="top">

                    06/20/2001


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$144.83</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Exner, Charles';
                    					document.getElementById('ids').value='958';
                    					sub();
                    					">
                    Exner, Charles
                    </a>

                    </td>
                    <td align="left" valign="top">Charles Exner for Parks</td>

                    <td align="left" valign="top">

                    08/07/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$240.00</td>
                    <td align="left" valign="top" >$53.19</td>
                    <td align="left" valign="top" >$186.81 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Faitek, Adam';
                    					document.getElementById('ids').value='925';
                    					sub();
                    					">
                    Faitek, Adam
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Adam Faitek</td>

                    <td align="left" valign="top">

                    02/28/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >13</td>
                    <td align="left" valign="top" >$17,540.00</td>
                    <td align="left" valign="top" >$16,285.93</td>
                    <td align="left" valign="top" >$1,254.07 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Farah, Mohamed';
                    					document.getElementById('ids').value='893';
                    					sub();
                    					">
                    Farah, Mohamed
                    </a>

                    </td>
                    <td align="left" valign="top">Friends for Farah</td>

                    <td align="left" valign="top">

                    10/28/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >9</td>
                    <td align="left" valign="top" >$12,962.46</td>
                    <td align="left" valign="top" >$20,732.70</td>
                    <td align="left" valign="top" >$2,396.51 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Felder, KerryJo';
                    					document.getElementById('ids').value='874';
                    					sub();
                    					">
                    Felder, KerryJo
                    </a>

                    </td>
                    <td align="left" valign="top">KerryJo 4 School Board</td>

                    <td align="left" valign="top">

                    03/18/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$358.34 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Fernando, Irene';
                    					document.getElementById('ids').value='978';
                    					sub();
                    					">
                    Fernando, Irene
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Irene</td>

                    <td align="left" valign="top">

                    10/03/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Fine, Bob';
                    					document.getElementById('ids').value='967';
                    					sub();
                    					">
                    Fine, Bob
                    </a>

                    </td>
                    <td align="left" valign="top">Fine for Parks Vol Comm</td>

                    <td align="left" valign="top">

                    08/25/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Fine, Bob';
                    					document.getElementById('ids').value='796';
                    					sub();
                    					">
                    Fine, Bob
                    </a>

                    </td>
                    <td align="left" valign="top">Fine for Mayor</td>

                    <td align="left" valign="top">

                    08/06/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Fine, Bob';
                    					document.getElementById('ids').value='659';
                    					sub();
                    					">
                    Fine, Bob
                    </a>

                    </td>
                    <td align="left" valign="top">Fine for Parks-At Large</td>

                    <td align="left" valign="top">

                    09/05/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$600.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Fleetham, Patrick';
                    					document.getElementById('ids').value='772';
                    					sub();
                    					">
                    Fleetham, Patrick
                    </a>

                    </td>
                    <td align="left" valign="top">Pat Fleetham 4 Mpls City Council</td>

                    <td align="left" valign="top">

                    04/16/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >9</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$67.47 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Fletcher, Steven';
                    					document.getElementById('ids').value='911';
                    					sub();
                    					">
                    Fletcher, Steven
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Fletcher</td>

                    <td align="left" valign="top">

                    01/09/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$21,767.88</td>
                    <td align="left" valign="top" >$17,661.39</td>
                    <td align="left" valign="top" >$4,106.49 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Flisrand, Janne';
                    					document.getElementById('ids').value='894';
                    					sub();
                    					">
                    Flisrand, Janne
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Janne</td>

                    <td align="left" valign="top">

                    11/10/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >7</td>
                    <td align="left" valign="top" >$43,224.18</td>
                    <td align="left" valign="top" >$38,779.55</td>
                    <td align="left" valign="top" >$23,745.59 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Flowers, Al';
                    					document.getElementById('ids').value='941';
                    					sub();
                    					">
                    Flowers, Al
                    </a>

                    </td>
                    <td align="left" valign="top">Truth to the People Campaign Committee</td>

                    <td align="left" valign="top">

                    04/19/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$5,571.68</td>
                    <td align="left" valign="top" >$3,821.82</td>
                    <td align="left" valign="top" >$1,749.86 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Flynn Forslund, Tiffini';
                    					document.getElementById('ids').value='914';
                    					sub();
                    					">
                    Flynn Forslund, Tiffini
                    </a>

                    </td>
                    <td align="left" valign="top">Vote Tiffini 2017</td>

                    <td align="left" valign="top">

                    01/30/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$1,627.25</td>
                    <td align="left" valign="top" >$1,618.34</td>
                    <td align="left" valign="top" >$8.91 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Forney, Meg';
                    					document.getElementById('ids').value='808';
                    					sub();
                    					">
                    Forney, Meg
                    </a>

                    </td>
                    <td align="left" valign="top">Meg Forney for Parks</td>

                    <td align="left" valign="top">

                    09/05/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$10,324.00</td>
                    <td align="left" valign="top" >$14,296.81</td>
                    <td align="left" valign="top" >$8,657.98 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Free, Addy';
                    					document.getElementById('ids').value='929';
                    					sub();
                    					">
                    Free, Addy
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Addy</td>

                    <td align="left" valign="top">

                    03/07/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$2,939.79</td>
                    <td align="left" valign="top" >$1,064.87</td>
                    <td align="left" valign="top" >$1,874.92 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Freeman, Daniel';
                    					document.getElementById('ids').value='732';
                    					sub();
                    					">
                    Freeman, Daniel
                    </a>

                    </td>
                    <td align="left" valign="top">Freeman Volunteer Committee</td>

                    <td align="left" valign="top">

                    07/12/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Three Rivers Park District</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$883.85 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Freeman, Michael O.';
                    					document.getElementById('ids').value='499';
                    					sub();
                    					">
                    Freeman, Michael O.
                    </a>

                    </td>
                    <td align="left" valign="top">Return Mike Freeman - Hennepin County Attorney</td>

                    <td align="left" valign="top">

                    09/09/2005


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >County Attorney</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$31,373.68 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='French, Londel';
                    					document.getElementById('ids').value='901';
                    					sub();
                    					">
                    French, Londel
                    </a>

                    </td>
                    <td align="left" valign="top">French for Parks</td>

                    <td align="left" valign="top">

                    12/19/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$7,638.29</td>
                    <td align="left" valign="top" >$7,256.93</td>
                    <td align="left" valign="top" >$1,105.26 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Frey, Jacob';
                    					document.getElementById('ids').value='742';
                    					sub();
                    					">
                    Frey, Jacob
                    </a>

                    </td>
                    <td align="left" valign="top">Jacob Frey for Our City</td>

                    <td align="left" valign="top">

                    10/05/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$359,878.75</td>
                    <td align="left" valign="top" >$244,199.07</td>
                    <td align="left" valign="top" >$293,306.88 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Frost, Larry';
                    					document.getElementById('ids').value='948';
                    					sub();
                    					">
                    Frost, Larry
                    </a>

                    </td>
                    <td align="left" valign="top">Frost for Council</td>

                    <td align="left" valign="top">

                    06/14/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$227.97</td>
                    <td align="left" valign="top" >$127.97</td>
                    <td align="left" valign="top" >$100.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gagnon, Rebecca';
                    					document.getElementById('ids').value='687';
                    					sub();
                    					">
                    Gagnon, Rebecca
                    </a>

                    </td>
                    <td align="left" valign="top">Rebecca Gagnon&#39;s Campaign Fund</td>

                    <td align="left" valign="top">

                    06/08/2010


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >At Large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$908.61 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gasca, Stephanie';
                    					document.getElementById('ids').value='906';
                    					sub();
                    					">
                    Gasca, Stephanie
                    </a>

                    </td>
                    <td align="left" valign="top">United for Stephanie</td>

                    <td align="left" valign="top">

                    12/23/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$8,975.75</td>
                    <td align="left" valign="top" >$5,332.09</td>
                    <td align="left" valign="top" >$4,050.70 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gates, Rich';
                    					document.getElementById('ids').value='855';
                    					sub();
                    					">
                    Gates, Rich
                    </a>

                    </td>
                    <td align="left" valign="top">Rich Gates for City Council</td>

                    <td align="left" valign="top">

                    09/02/2014


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Brooklyn Park</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >Central</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gers, Charlie';
                    					document.getElementById('ids').value='966';
                    					sub();
                    					">
                    Gers, Charlie
                    </a>

                    </td>
                    <td align="left" valign="top">Charlie for Mayor</td>

                    <td align="left" valign="top">

                    08/21/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gibbs, John';
                    					document.getElementById('ids').value='694';
                    					sub();
                    					">
                    Gibbs, John
                    </a>

                    </td>
                    <td align="left" valign="top">John Gibbs Volunteer Committee</td>

                    <td align="left" valign="top">

                    09/13/2010


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Three Rivers Park District</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$19.41 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Glidden, Elizabeth';
                    					document.getElementById('ids').value='409';
                    					sub();
                    					">
                    Glidden, Elizabeth
                    </a>

                    </td>
                    <td align="left" valign="top">Volunteers for Elizabeth Glidden</td>

                    <td align="left" valign="top">

                    01/03/2004


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >8</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$3,665.58 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Goettel, Debbie';
                    					document.getElementById('ids').value='877';
                    					sub();
                    					">
                    Goettel, Debbie
                    </a>

                    </td>
                    <td align="left" valign="top">Debbie Goettel for Hennepin County</td>

                    <td align="left" valign="top">

                    05/18/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$10,245.00</td>
                    <td align="left" valign="top" >$10,530.90</td>
                    <td align="left" valign="top" >$8,244.38 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Goodman, Lisa';
                    					document.getElementById('ids').value='58';
                    					sub();
                    					">
                    Goodman, Lisa
                    </a>

                    </td>
                    <td align="left" valign="top">Friends for Lisa Goodman</td>

                    <td align="left" valign="top">

                    02/07/1997


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >7</td>
                    <td align="left" valign="top" >$72,397.82</td>
                    <td align="left" valign="top" >$63,374.71</td>
                    <td align="left" valign="top" >$142,188.28 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gordon, Cam';
                    					document.getElementById('ids').value='230';
                    					sub();
                    					">
                    Gordon, Cam
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Cam Gordon</td>

                    <td align="left" valign="top">

                    12/28/2000


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$301.00</td>
                    <td align="left" valign="top" >$2,937.03</td>
                    <td align="left" valign="top" >$5,904.61 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Greene, Marion';
                    					document.getElementById('ids').value='832';
                    					sub();
                    					">
                    Greene, Marion
                    </a>

                    </td>
                    <td align="left" valign="top">Marion for Hennepin</td>

                    <td align="left" valign="top">

                    12/06/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$35,990.58 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Gunyou, John';
                    					document.getElementById('ids').value='722';
                    					sub();
                    					">
                    Gunyou, John
                    </a>

                    </td>
                    <td align="left" valign="top">Committee to Elect John Gunyou</td>

                    <td align="left" valign="top">

                    06/08/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Three Rivers Park District</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,200.90 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hansen, Dana';
                    					document.getElementById('ids').value='964';
                    					sub();
                    					">
                    Hansen, Dana
                    </a>

                    </td>
                    <td align="left" valign="top">Dana Hansen for Ward 4</td>

                    <td align="left" valign="top">

                    08/14/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hanson, Amy';
                    					document.getElementById('ids').value='884';
                    					sub();
                    					">
                    Hanson, Amy
                    </a>

                    </td>
                    <td align="left" valign="top">Amy S Hanson for City Council</td>

                    <td align="left" valign="top">

                    06/16/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Brooklyn Park</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >West</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$371.81 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Harp, Sandra';
                    					document.getElementById('ids').value='86';
                    					sub();
                    					">
                    Harp, Sandra
                    </a>

                    </td>
                    <td align="left" valign="top">Sandra Harp Volunteer Committee (School Board)</td>

                    <td align="left" valign="top">

                    09/08/1987


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hassan, Abdikadir';
                    					document.getElementById('ids').value='902';
                    					sub();
                    					">
                    Hassan, Abdikadir
                    </a>

                    </td>
                    <td align="left" valign="top">AK Hassan for Minneapolis Parks</td>

                    <td align="left" valign="top">

                    12/20/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$8,656.93</td>
                    <td align="left" valign="top" >$7,985.67</td>
                    <td align="left" valign="top" >$671.26 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hayden, John';
                    					document.getElementById('ids').value='942';
                    					sub();
                    					">
                    Hayden, John
                    </a>

                    </td>
                    <td align="left" valign="top">Hayden for Ward One</td>

                    <td align="left" valign="top">

                    04/24/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$4,240.02</td>
                    <td align="left" valign="top" >$3,903.20</td>
                    <td align="left" valign="top" >$336.82 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Henry, Russ';
                    					document.getElementById('ids').value='872';
                    					sub();
                    					">
                    Henry, Russ
                    </a>

                    </td>
                    <td align="left" valign="top">Russ Henry for Park Board</td>

                    <td align="left" valign="top">

                    03/03/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$9,051.00</td>
                    <td align="left" valign="top" >$10,105.48</td>
                    <td align="left" valign="top" >$1,631.36 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Higgins, Linda';
                    					document.getElementById('ids').value='709';
                    					sub();
                    					">
                    Higgins, Linda
                    </a>

                    </td>
                    <td align="left" valign="top">Volunteers for Higgins</td>

                    <td align="left" valign="top">

                    03/02/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$10,457.10 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Higgins, Susan';
                    					document.getElementById('ids').value='919';
                    					sub();
                    					">
                    Higgins, Susan
                    </a>

                    </td>
                    <td align="left" valign="top">Friends of Susan for Ward 3</td>

                    <td align="left" valign="top">

                    02/03/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hoch, Tom';
                    					document.getElementById('ids').value='920';
                    					sub();
                    					">
                    Hoch, Tom
                    </a>

                    </td>
                    <td align="left" valign="top">Tom Hoch for Minneapolis</td>

                    <td align="left" valign="top">

                    02/09/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$442,082.61</td>
                    <td align="left" valign="top" >$296,508.63</td>
                    <td align="left" valign="top" >$145,573.98 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hodges, Betsy';
                    					document.getElementById('ids').value='746';
                    					sub();
                    					">
                    Hodges, Betsy
                    </a>

                    </td>
                    <td align="left" valign="top">Hodges for Mayor</td>

                    <td align="left" valign="top">

                    11/28/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$258,137.66</td>
                    <td align="left" valign="top" >$241,406.75</td>
                    <td align="left" valign="top" >$57,901.12 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hodges, Betsy';
                    					document.getElementById('ids').value='401';
                    					sub();
                    					">
                    Hodges, Betsy
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Hodges</td>

                    <td align="left" valign="top">

                    12/08/2004


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >13</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$2,314.86 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Hogan, Devin';
                    					document.getElementById('ids').value='905';
                    					sub();
                    					">
                    Hogan, Devin
                    </a>

                    </td>
                    <td align="left" valign="top">Devin for Parks</td>

                    <td align="left" valign="top">

                    12/21/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$4,659.76</td>
                    <td align="left" valign="top" >$5,433.53</td>
                    <td align="left" valign="top" >$31.23 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Holsinger, David';
                    					document.getElementById('ids').value='959';
                    					sub();
                    					">
                    Holsinger, David
                    </a>

                    </td>
                    <td align="left" valign="top">Committee to Elect David Holsinger</td>

                    <td align="left" valign="top">

                    08/07/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >8</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Honerbrink, Jonathan';
                    					document.getElementById('ids').value='957';
                    					sub();
                    					">
                    Honerbrink, Jonathan
                    </a>

                    </td>
                    <td align="left" valign="top">Jonathan for Minneapolis</td>

                    <td align="left" valign="top">

                    08/01/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$5,000.00</td>
                    <td align="left" valign="top" >$3,108.54</td>
                    <td align="left" valign="top" >$1,891.46 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Inz, Nelson';
                    					document.getElementById('ids').value='838';
                    					sub();
                    					">
                    Inz, Nelson
                    </a>

                    </td>
                    <td align="left" valign="top">Nelson Inz for Schools</td>

                    <td align="left" valign="top">

                    02/10/2014


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$2,021.06 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Jacobson, Lisa';
                    					document.getElementById('ids').value='882';
                    					sub();
                    					">
                    Jacobson, Lisa
                    </a>

                    </td>
                    <td align="left" valign="top">Lisa Jacobson for City Council</td>

                    <td align="left" valign="top">

                    06/10/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Brooklyn Park</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >East</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$36.04 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Jenkins, Andrea';
                    					document.getElementById('ids').value='904';
                    					sub();
                    					">
                    Jenkins, Andrea
                    </a>

                    </td>
                    <td align="left" valign="top">Andrea Jenkins for Ward 8</td>

                    <td align="left" valign="top">

                    12/22/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >8</td>
                    <td align="left" valign="top" >$25,512.00</td>
                    <td align="left" valign="top" >$16,849.97</td>
                    <td align="left" valign="top" >$12,454.42 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Jentzen, Ginger';
                    					document.getElementById('ids').value='918';
                    					sub();
                    					">
                    Jentzen, Ginger
                    </a>

                    </td>
                    <td align="left" valign="top">Vote Ginger Jentzen</td>

                    <td align="left" valign="top">

                    02/02/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$60,155.20</td>
                    <td align="left" valign="top" >$38,254.50</td>
                    <td align="left" valign="top" >$21,900.70 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Johnson, Andrew';
                    					document.getElementById('ids').value='762';
                    					sub();
                    					">
                    Johnson, Andrew
                    </a>

                    </td>
                    <td align="left" valign="top">Andrew Johnson for Minneapolis City Council</td>

                    <td align="left" valign="top">

                    02/15/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >12</td>
                    <td align="left" valign="top" >$18,235.00</td>
                    <td align="left" valign="top" >$16,073.12</td>
                    <td align="left" valign="top" >$48,028.69 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Johnson, Barbara';
                    					document.getElementById('ids').value='116';
                    					sub();
                    					">
                    Johnson, Barbara
                    </a>

                    </td>
                    <td align="left" valign="top">Barb Johnson Volunteer Committee (Ward 4)</td>

                    <td align="left" valign="top">

                    02/11/1997


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$41,305.00</td>
                    <td align="left" valign="top" >$52,543.00</td>
                    <td align="left" valign="top" >$40,934.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Johnson, Jeff R';
                    					document.getElementById('ids').value='566';
                    					sub();
                    					">
                    Johnson, Jeff R
                    </a>

                    </td>
                    <td align="left" valign="top">Jeff Johnson for County Commissioner</td>

                    <td align="left" valign="top">

                    06/14/2007


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >7</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$3,067.26 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Johnson, Randy';
                    					document.getElementById('ids').value='138';
                    					sub();
                    					">
                    Johnson, Randy
                    </a>

                    </td>
                    <td align="left" valign="top">Friends of Randy Johnson (Commissioner 5)</td>

                    <td align="left" valign="top">

                    06/05/1980


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$11,587.13 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Jourdain, Ira';
                    					document.getElementById('ids').value='867';
                    					sub();
                    					">
                    Jourdain, Ira
                    </a>

                    </td>
                    <td align="left" valign="top">Ira Jourdain for District 6</td>

                    <td align="left" valign="top">

                    12/17/2015


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,798.71 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Kahn, Bill';
                    					document.getElementById('ids').value='825';
                    					sub();
                    					">
                    Kahn, Bill
                    </a>

                    </td>
                    <td align="left" valign="top">Last Minneapolis Mayor Committee</td>

                    <td align="left" valign="top">

                    10/29/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Kane, April';
                    					document.getElementById('ids').value='969';
                    					sub();
                    					">
                    Kane, April
                    </a>

                    </td>
                    <td align="left" valign="top">April Kane</td>

                    <td align="left" valign="top">

                    08/25/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >8</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Klevan Schmitz, Lenny';
                    					document.getElementById('ids').value='945';
                    					sub();
                    					">
                    Klevan Schmitz, Lenny
                    </a>

                    </td>
                    <td align="left" valign="top">Klevan Schmitz for Council</td>

                    <td align="left" valign="top">

                    06/08/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$3,024.45</td>
                    <td align="left" valign="top" >$1,126.51</td>
                    <td align="left" valign="top" >$1,897.94 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Kovacs, Joseph';
                    					document.getElementById('ids').value='940';
                    					sub();
                    					">
                    Kovacs, Joseph
                    </a>

                    </td>
                    <td align="left" valign="top">Kovacs for City Council</td>

                    <td align="left" valign="top">

                    04/19/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >7</td>
                    <td align="left" valign="top" >$817.21</td>
                    <td align="left" valign="top" >$368.45</td>
                    <td align="left" valign="top" >$448.76 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Krueger, Rod';
                    					document.getElementById('ids').value='76';
                    					sub();
                    					">
                    Krueger, Rod
                    </a>

                    </td>
                    <td align="left" valign="top">Krueger for Library Board</td>

                    <td align="left" valign="top">

                    07/26/1993


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Library Board</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1.89 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Leininger, Larry';
                    					document.getElementById('ids').value='485';
                    					sub();
                    					">
                    Leininger, Larry
                    </a>

                    </td>
                    <td align="left" valign="top">White Working Mans Party</td>

                    <td align="left" valign="top">

                    08/08/2005


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Levy  Pounds, Nekima';
                    					document.getElementById('ids').value='903';
                    					sub();
                    					">
                    Levy  Pounds, Nekima
                    </a>

                    </td>
                    <td align="left" valign="top">Minneapolis for Nekima</td>

                    <td align="left" valign="top">

                    12/22/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$20,255.00</td>
                    <td align="left" valign="top" >$20,178.00</td>
                    <td align="left" valign="top" >$4,095.89 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Lewis, Cheryl';
                    					document.getElementById('ids').value='954';
                    					sub();
                    					">
                    Lewis, Cheryl
                    </a>

                    </td>
                    <td align="left" valign="top">Cheryl for City Council</td>

                    <td align="left" valign="top">

                    07/07/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$280.00</td>
                    <td align="left" valign="top" >$260.24</td>
                    <td align="left" valign="top" >$19.76 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Lischeid, Ronald';
                    					document.getElementById('ids').value='973';
                    					sub();
                    					">
                    Lischeid, Ronald
                    </a>

                    </td>
                    <td align="left" valign="top">Ron4MayorMpls</td>

                    <td align="left" valign="top">

                    08/30/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Lowman, Dwayne';
                    					document.getElementById('ids').value='788';
                    					sub();
                    					">
                    Lowman, Dwayne
                    </a>

                    </td>
                    <td align="left" valign="top">Campaign Fund of Dwayne A Lowman for Bloomington</td>

                    <td align="left" valign="top">

                    06/24/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$654.73 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Lundeen, Bruce';
                    					document.getElementById('ids').value='960';
                    					sub();
                    					">
                    Lundeen, Bruce
                    </a>

                    </td>
                    <td align="left" valign="top">Bruce for City Council</td>

                    <td align="left" valign="top">

                    08/08/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >10</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Martin, Patrick';
                    					document.getElementById('ids').value='923';
                    					sub();
                    					">
                    Martin, Patrick
                    </a>

                    </td>
                    <td align="left" valign="top">Patrick Martin for Bloomington</td>

                    <td align="left" valign="top">

                    02/27/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$2,440.12</td>
                    <td align="left" valign="top" >$1,338.84</td>
                    <td align="left" valign="top" >$1,101.28 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Mauter, Erica';
                    					document.getElementById('ids').value='900';
                    					sub();
                    					">
                    Mauter, Erica
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Erica Mauter</td>

                    <td align="left" valign="top">

                    12/16/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >11</td>
                    <td align="left" valign="top" >$15,073.22</td>
                    <td align="left" valign="top" >$10,733.80</td>
                    <td align="left" valign="top" >$8,777.42 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='McClellan, Johnathon';
                    					document.getElementById('ids').value='863';
                    					sub();
                    					">
                    McClellan, Johnathon
                    </a>

                    </td>
                    <td align="left" valign="top">McClellan For Bloomington</td>

                    <td align="left" valign="top">

                    06/02/2015


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$221.22 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Mclaughlin, Peter';
                    					document.getElementById('ids').value='407';
                    					sub();
                    					">
                    Mclaughlin, Peter
                    </a>

                    </td>
                    <td align="left" valign="top">Mclaughlin for Mayor</td>

                    <td align="left" valign="top">

                    12/23/2004


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$568.38 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='McLaughlin, Peter';
                    					document.getElementById('ids').value='84';
                    					sub();
                    					">
                    McLaughlin, Peter
                    </a>

                    </td>
                    <td align="left" valign="top">Friends of Peter Mclaughlin</td>

                    <td align="left" valign="top">

                    02/27/1990


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$22,399.03 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Menz, Billly';
                    					document.getElementById('ids').value='953';
                    					sub();
                    					">
                    Menz, Billly
                    </a>

                    </td>
                    <td align="left" valign="top">Menz 4 Park Board</td>

                    <td align="left" valign="top">

                    06/26/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$2,200.00</td>
                    <td align="left" valign="top" >$1,349.63</td>
                    <td align="left" valign="top" >$850.37 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Meyer, Christopher';
                    					document.getElementById('ids').value='934';
                    					sub();
                    					">
                    Meyer, Christopher
                    </a>

                    </td>
                    <td align="left" valign="top">Meyer for Parks</td>

                    <td align="left" valign="top">

                    03/22/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$5,215.00</td>
                    <td align="left" valign="top" >$4,838.07</td>
                    <td align="left" valign="top" >$376.93 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Miller, Bob';
                    					document.getElementById('ids').value='595';
                    					sub();
                    					">
                    Miller, Bob
                    </a>

                    </td>
                    <td align="left" valign="top">Bob Miller for Mayor</td>

                    <td align="left" valign="top">

                    11/12/2008


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,340.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Mohamed, Abdi \'Gurhan\'';
                    					document.getElementById('ids').value='896';
                    					sub();
                    					">
                    Mohamed, Abdi &quot;Gurhan&quot;
                    </a>

                    </td>
                    <td align="left" valign="top">Gurhan for Parks</td>

                    <td align="left" valign="top">

                    11/30/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$2,950.00</td>
                    <td align="left" valign="top" >$12,471.05</td>
                    <td align="left" valign="top" >$511.45 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Moller, Andrew';
                    					document.getElementById('ids').value='881';
                    					sub();
                    					">
                    Moller, Andrew
                    </a>

                    </td>
                    <td align="left" valign="top">Andrew K Moller Election Committee</td>

                    <td align="left" valign="top">

                    06/09/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$44.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Moore, Ty';
                    					document.getElementById('ids').value='763';
                    					sub();
                    					">
                    Moore, Ty
                    </a>

                    </td>
                    <td align="left" valign="top">Ty Moore for City Council</td>

                    <td align="left" valign="top">

                    02/20/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >9</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$66.28 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Musich, Steffanie';
                    					document.getElementById('ids').value='753';
                    					sub();
                    					">
                    Musich, Steffanie
                    </a>

                    </td>
                    <td align="left" valign="top">Musich for Parks</td>

                    <td align="left" valign="top">

                    01/03/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$1,070.00</td>
                    <td align="left" valign="top" >$1,011.29</td>
                    <td align="left" valign="top" >$1,899.49 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Nelson, Shawn';
                    					document.getElementById('ids').value='947';
                    					sub();
                    					">
                    Nelson, Shawn
                    </a>

                    </td>
                    <td align="left" valign="top">Nelson for Bloomington</td>

                    <td align="left" valign="top">

                    06/09/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$3,720.00</td>
                    <td align="left" valign="top" >$2,113.97</td>
                    <td align="left" valign="top" >$1,606.03 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Noor, Mohamud';
                    					document.getElementById('ids').value='916';
                    					sub();
                    					">
                    Noor, Mohamud
                    </a>

                    </td>
                    <td align="left" valign="top">Noor for Ward 6</td>

                    <td align="left" valign="top">

                    01/31/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$23,472.60</td>
                    <td align="left" valign="top" >$17,072.93</td>
                    <td align="left" valign="top" >$6,399.67 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Nordyke, Tom';
                    					document.getElementById('ids').value='461';
                    					sub();
                    					">
                    Nordyke, Tom
                    </a>

                    </td>
                    <td align="left" valign="top">Nordyke for Minneapolis Parks Committee</td>

                    <td align="left" valign="top">

                    04/21/2005


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Nordyke, Tom';
                    					document.getElementById('ids').value='976';
                    					sub();
                    					">
                    Nordyke, Tom
                    </a>

                    </td>
                    <td align="left" valign="top">Nordyke for Minneapolis Parks</td>

                    <td align="left" valign="top">

                    09/13/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Oleson, Jon';
                    					document.getElementById('ids').value='792';
                    					sub();
                    					">
                    Oleson, Jon
                    </a>

                    </td>
                    <td align="left" valign="top">Oleson for IV Principal Campaign Committee</td>

                    <td align="left" valign="top">

                    07/16/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$50.00</td>
                    <td align="left" valign="top" >$35.00</td>
                    <td align="left" valign="top" >$40.04 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Olson, Jon Christopher';
                    					document.getElementById('ids').value='203';
                    					sub();
                    					">
                    Olson, Jon Christopher
                    </a>

                    </td>
                    <td align="left" valign="top">Jon Olson Volunteer Committee Dist 2</td>

                    <td align="left" valign="top">

                    07/03/2001


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$253.77 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Opat, Michael J.';
                    					document.getElementById('ids').value='238';
                    					sub();
                    					">
                    Opat, Michael J.
                    </a>

                    </td>
                    <td align="left" valign="top">Mike Opat Volunteer Committee</td>

                    <td align="left" valign="top">

                    12/19/1991


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$17,447.64 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Palmisano, Linea';
                    					document.getElementById('ids').value='755';
                    					sub();
                    					">
                    Palmisano, Linea
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Linea</td>

                    <td align="left" valign="top">

                    01/07/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >13</td>
                    <td align="left" valign="top" >$16,216.00</td>
                    <td align="left" valign="top" >$20,801.60</td>
                    <td align="left" valign="top" >$35,777.97 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Parker, Troy';
                    					document.getElementById('ids').value='608';
                    					sub();
                    					">
                    Parker, Troy
                    </a>

                    </td>
                    <td align="left" valign="top">Troy Parker for 4th Ward City Council</td>

                    <td align="left" valign="top">

                    02/19/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$14.94 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Parks, Terry';
                    					document.getElementById('ids').value='845';
                    					sub();
                    					">
                    Parks, Terry
                    </a>

                    </td>
                    <td align="left" valign="top">Terry Parks for City Council</td>

                    <td align="left" valign="top">

                    05/30/2014


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Brooklyn Park</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >East</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$49.75 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Peer, Steve';
                    					document.getElementById('ids').value='797';
                    					sub();
                    					">
                    Peer, Steve
                    </a>

                    </td>
                    <td align="left" valign="top">Peer for City Council</td>

                    <td align="left" valign="top">

                    08/08/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$-419.62 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Perry, Matt';
                    					document.getElementById('ids').value='749';
                    					sub();
                    					">
                    Perry, Matt
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Perry</td>

                    <td align="left" valign="top">

                    12/07/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >13</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$133.41 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Pessenda, Jillia';
                    					document.getElementById('ids').value='897';
                    					sub();
                    					">
                    Pessenda, Jillia
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Jillia</td>

                    <td align="left" valign="top">

                    11/30/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$34,073.00</td>
                    <td align="left" valign="top" >$31,348.63</td>
                    <td align="left" valign="top" >$11,482.22 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Pierson, Cordelia';
                    					document.getElementById('ids').value='910';
                    					sub();
                    					">
                    Pierson, Cordelia
                    </a>

                    </td>
                    <td align="left" valign="top">Cordelia Pierson for City Council</td>

                    <td align="left" valign="top">

                    01/06/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Pilotta, Nick';
                    					document.getElementById('ids').value='928';
                    					sub();
                    					">
                    Pilotta, Nick
                    </a>

                    </td>
                    <td align="left" valign="top">L.A. Nik for Mayor</td>

                    <td align="left" valign="top">

                    03/03/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Pree-Stinson, Samantha';
                    					document.getElementById('ids').value='924';
                    					sub();
                    					">
                    Pree-Stinson, Samantha
                    </a>

                    </td>
                    <td align="left" valign="top">Campaign to Elect Samantha Pree-Stinson</td>

                    <td align="left" valign="top">

                    02/23/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$21,540.00</td>
                    <td align="left" valign="top" >$13,135.28</td>
                    <td align="left" valign="top" >$8,404.72 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Quincy, John';
                    					document.getElementById('ids').value='603';
                    					sub();
                    					">
                    Quincy, John
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for John Quincy</td>

                    <td align="left" valign="top">

                    12/31/2008


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >11</td>
                    <td align="left" valign="top" >$26,491.17</td>
                    <td align="left" valign="top" >$31,513.37</td>
                    <td align="left" valign="top" >$17,987.54 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Rahman, Aswar';
                    					document.getElementById('ids').value='921';
                    					sub();
                    					">
                    Rahman, Aswar
                    </a>

                    </td>
                    <td align="left" valign="top">Aswar for Mayor</td>

                    <td align="left" valign="top">

                    02/14/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$13,625.00</td>
                    <td align="left" valign="top" >$9,775.25</td>
                    <td align="left" valign="top" >$3,849.75 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Reich, Kevin';
                    					document.getElementById('ids').value='604';
                    					sub();
                    					">
                    Reich, Kevin
                    </a>

                    </td>
                    <td align="left" valign="top">Reich for Ward 1</td>

                    <td align="left" valign="top">

                    01/14/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$44,450.00</td>
                    <td align="left" valign="top" >$57,674.62</td>
                    <td align="left" valign="top" >$13,488.40 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Reichert, William';
                    					document.getElementById('ids').value='885';
                    					sub();
                    					">
                    Reichert, William
                    </a>

                    </td>
                    <td align="left" valign="top">Elect Reichert</td>

                    <td align="left" valign="top">

                    06/17/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$36.13 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Remnitz, Josh';
                    					document.getElementById('ids').value='719';
                    					sub();
                    					">
                    Remnitz, Josh
                    </a>

                    </td>
                    <td align="left" valign="top">Josh Remnitz for Minneapolis School Board</td>

                    <td align="left" valign="top">

                    05/31/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$2,824.01 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Romanishan, Saralyn';
                    					document.getElementById('ids').value='951';
                    					sub();
                    					">
                    Romanishan, Saralyn
                    </a>

                    </td>
                    <td align="left" valign="top">Saralyn Romanishan for Ward 10</td>

                    <td align="left" valign="top">

                    06/23/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >10</td>
                    <td align="left" valign="top" >$1,605.00</td>
                    <td align="left" valign="top" >$559.20</td>
                    <td align="left" valign="top" >$1,045.80 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Rosenfeld, David';
                    					document.getElementById('ids').value='943';
                    					sub();
                    					">
                    Rosenfeld, David
                    </a>

                    </td>
                    <td align="left" valign="top">MN Socialist Workers Campaign 2017</td>

                    <td align="left" valign="top">

                    04/25/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$410.35</td>
                    <td align="left" valign="top" >$180.37</td>
                    <td align="left" valign="top" >$229.98 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Samuels, Don';
                    					document.getElementById('ids').value='850';
                    					sub();
                    					">
                    Samuels, Don
                    </a>

                    </td>
                    <td align="left" valign="top">Samuels for School Board</td>

                    <td align="left" valign="top">

                    07/03/2014


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >At Large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,246.09 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Samuels, Donald';
                    					document.getElementById('ids').value='317';
                    					sub();
                    					">
                    Samuels, Donald
                    </a>

                    </td>
                    <td align="left" valign="top">Samuels for Council</td>

                    <td align="left" valign="top">

                    12/12/2002


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$4,061.84 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Sayles Belton, Sharon';
                    					document.getElementById('ids').value='90';
                    					sub();
                    					">
                    Sayles Belton, Sharon
                    </a>

                    </td>
                    <td align="left" valign="top">Belton for Mayor</td>

                    <td align="left" valign="top">

                    02/10/2000


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$23.63 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Schiff, Gary';
                    					document.getElementById('ids').value='78';
                    					sub();
                    					">
                    Schiff, Gary
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Gary Schiff</td>

                    <td align="left" valign="top">

                    02/18/2000


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >9</td>
                    <td align="left" valign="top" >$48,595.00</td>
                    <td align="left" valign="top" >$43,532.87</td>
                    <td align="left" valign="top" >$5,062.13 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Schiff, Gary';
                    					document.getElementById('ids').value='751';
                    					sub();
                    					">
                    Schiff, Gary
                    </a>

                    </td>
                    <td align="left" valign="top">Gary Schiff for Mayor</td>

                    <td align="left" valign="top">

                    12/12/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$27,107.23 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Schlosser, Robert';
                    					document.getElementById('ids').value='965';
                    					sub();
                    					">
                    Schlosser, Robert
                    </a>

                    </td>
                    <td align="left" valign="top">Upright Citezens League</td>

                    <td align="left" valign="top">

                    08/15/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Schorn, David';
                    					document.getElementById('ids').value='952';
                    					sub();
                    					">
                    Schorn, David
                    </a>

                    </td>
                    <td align="left" valign="top">Schorn for Ward 10</td>

                    <td align="left" valign="top">

                    06/26/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >10</td>
                    <td align="left" valign="top" >$100.00</td>
                    <td align="left" valign="top" >$341.44</td>
                    <td align="left" valign="top" >$-241.44 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Schroeder, Jeremy';
                    					document.getElementById('ids').value='891';
                    					sub();
                    					">
                    Schroeder, Jeremy
                    </a>

                    </td>
                    <td align="left" valign="top">Jeremy for Minneapolis</td>

                    <td align="left" valign="top">

                    10/05/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >11</td>
                    <td align="left" valign="top" >$11,677.00</td>
                    <td align="left" valign="top" >$5,982.73</td>
                    <td align="left" valign="top" >$9,174.56 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Scott, Traci';
                    					document.getElementById('ids').value='27';
                    					sub();
                    					">
                    Scott, Traci
                    </a>

                    </td>
                    <td align="left" valign="top">Traci Scott Volunteer Committee</td>

                    <td align="left" valign="top">

                    06/25/2001


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$561.46 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Severson, Kale';
                    					document.getElementById('ids').value='778';
                    					sub();
                    					">
                    Severson, Kale
                    </a>

                    </td>
                    <td align="left" valign="top">Vote Kale</td>

                    <td align="left" valign="top">

                    05/03/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$1,054.00</td>
                    <td align="left" valign="top" >$959.80</td>
                    <td align="left" valign="top" >$671.31 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Shroyer, Bill';
                    					document.getElementById('ids').value='944';
                    					sub();
                    					">
                    Shroyer, Bill
                    </a>

                    </td>
                    <td align="left" valign="top">Bill for Minneapolis Parks</td>

                    <td align="left" valign="top">

                    06/06/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$1,283.00</td>
                    <td align="left" valign="top" >$354.14</td>
                    <td align="left" valign="top" >$928.86 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Smith  Baker, Chanda';
                    					document.getElementById('ids').value='680';
                    					sub();
                    					">
                    Smith  Baker, Chanda
                    </a>

                    </td>
                    <td align="left" valign="top">Chanda Smith Baker for Public Schools</td>

                    <td align="left" valign="top">

                    03/18/2010


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >School Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,709.82 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Smithrud, Roger';
                    					document.getElementById('ids').value='673';
                    					sub();
                    					">
                    Smithrud, Roger
                    </a>

                    </td>
                    <td align="left" valign="top">Smithrud for Ward 5</td>

                    <td align="left" valign="top">

                    11/02/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Smithrud, Roger';
                    					document.getElementById('ids').value='692';
                    					sub();
                    					">
                    Smithrud, Roger
                    </a>

                    </td>
                    <td align="left" valign="top">Smithrud for Commissioner</td>

                    <td align="left" valign="top">

                    07/09/2010


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Commissioner</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$36.37 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Spann, Cathy';
                    					document.getElementById('ids').value='939';
                    					sub();
                    					">
                    Spann, Cathy
                    </a>

                    </td>
                    <td align="left" valign="top">Spann for Ward 5</td>

                    <td align="left" valign="top">

                    04/13/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$2,759.15</td>
                    <td align="left" valign="top" >$2,769.15</td>
                    <td align="left" valign="top" >$-10.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Sparrow, Captain Jack';
                    					document.getElementById('ids').value='935';
                    					sub();
                    					">
                    Sparrow, Captain Jack
                    </a>

                    </td>
                    <td align="left" valign="top">Captain Jack Sparrow Campaign Committee</td>

                    <td align="left" valign="top">

                    03/28/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$100.00</td>
                    <td align="left" valign="top" >$100.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Spencer, Eldon';
                    					document.getElementById('ids').value='955';
                    					sub();
                    					">
                    Spencer, Eldon
                    </a>

                    </td>
                    <td align="left" valign="top">Eldon Spencer for Council</td>

                    <td align="left" valign="top">

                    07/05/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$3,700.00</td>
                    <td align="left" valign="top" >$1,621.98</td>
                    <td align="left" valign="top" >$2,078.02 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Stanek, Richard W';
                    					document.getElementById('ids').value='511';
                    					sub();
                    					">
                    Stanek, Richard W
                    </a>

                    </td>
                    <td align="left" valign="top">Sheriff Stanek Volunteer Committee</td>

                    <td align="left" valign="top">

                    11/01/2005


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Sheriff</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$93,683.25 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Steele, Penny';
                    					document.getElementById('ids').value='731';
                    					sub();
                    					">
                    Steele, Penny
                    </a>

                    </td>
                    <td align="left" valign="top">Steele for Parks Committee</td>

                    <td align="left" valign="top">

                    07/12/2012


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Hennepin County</td>
                    <td align="left" valign="top" >Three Rivers Park District</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$803.08 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Sullentrop, Bob';
                    					document.getElementById('ids').value='971';
                    					sub();
                    					">
                    Sullentrop, Bob
                    </a>

                    </td>
                    <td align="left" valign="top">Bob Sullentrop for Park Board</td>

                    <td align="left" valign="top">

                    08/28/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Tabb, Anita';
                    					document.getElementById('ids').value='616';
                    					sub();
                    					">
                    Tabb, Anita
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Anita</td>

                    <td align="left" valign="top">

                    03/03/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$6,288.33 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Tate, Michael';
                    					document.getElementById('ids').value='917';
                    					sub();
                    					">
                    Tate, Michael
                    </a>

                    </td>
                    <td align="left" valign="top">Tate for Parks</td>

                    <td align="left" valign="top">

                    02/01/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >2</td>
                    <td align="left" valign="top" >$5,800.00</td>
                    <td align="left" valign="top" >$3,515.39</td>
                    <td align="left" valign="top" >$2,284.61 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Velez, Jose';
                    					document.getElementById('ids').value='605';
                    					sub();
                    					">
                    Velez, Jose
                    </a>

                    </td>
                    <td align="left" valign="top">Citizens for Jose Velez</td>

                    <td align="left" valign="top">

                    01/14/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$262.76 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Vetaw, Latrisha';
                    					document.getElementById('ids').value='963';
                    					sub();
                    					">
                    Vetaw, Latrisha
                    </a>

                    </td>
                    <td align="left" valign="top">Latrisha Vetaw for Parks</td>

                    <td align="left" valign="top">

                    08/14/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Vlaisavljevich, Kim';
                    					document.getElementById('ids').value='630';
                    					sub();
                    					">
                    Vlaisavljevich, Kim
                    </a>

                    </td>
                    <td align="left" valign="top">Kim for Bloomington</td>

                    <td align="left" valign="top">

                    07/06/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$1,050.00</td>
                    <td align="left" valign="top" >$177.19</td>
                    <td align="left" valign="top" >$873.81 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Vreeland, Scott';
                    					document.getElementById('ids').value='228';
                    					sub();
                    					">
                    Vreeland, Scott
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Scott Vreeland</td>

                    <td align="left" valign="top">

                    12/28/2004


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >3</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$1,447.09 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Vreeland, Scott';
                    					document.getElementById('ids').value='930';
                    					sub();
                    					">
                    Vreeland, Scott
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Scott Vreeland for Park Board At-Large</td>

                    <td align="left" valign="top">

                    03/14/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Warsame, Abdi';
                    					document.getElementById('ids').value='754';
                    					sub();
                    					">
                    Warsame, Abdi
                    </a>

                    </td>
                    <td align="left" valign="top">Warsame Volunteer Committee</td>

                    <td align="left" valign="top">

                    01/03/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$20,152.76</td>
                    <td align="left" valign="top" >$61,955.41</td>
                    <td align="left" valign="top" >$53,179.52 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Wefel, Zachary';
                    					document.getElementById('ids').value='898';
                    					sub();
                    					">
                    Wefel, Zachary
                    </a>

                    </td>
                    <td align="left" valign="top">Wefel for Ward 1 Campaign Committee</td>

                    <td align="left" valign="top">

                    12/01/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$-28.03 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Wheeler, David';
                    					document.getElementById('ids').value='627';
                    					sub();
                    					">
                    Wheeler, David
                    </a>

                    </td>
                    <td align="left" valign="top">Volunteers for Wheeler</td>

                    <td align="left" valign="top">

                    05/21/2009


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Estimate &amp; Tax Board</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$250.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$499.96 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='White, Terry';
                    					document.getElementById('ids').value='936';
                    					sub();
                    					">
                    White, Terry
                    </a>

                    </td>
                    <td align="left" valign="top">Neighbors for Terry</td>

                    <td align="left" valign="top">

                    04/06/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >8</td>
                    <td align="left" valign="top" >$1,960.00</td>
                    <td align="left" valign="top" >$702.33</td>
                    <td align="left" valign="top" >$1,257.67 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Wielinski, Liz';
                    					document.getElementById('ids').value='599';
                    					sub();
                    					">
                    Wielinski, Liz
                    </a>

                    </td>
                    <td align="left" valign="top">Wielinski for Parks Volunteer Committee</td>

                    <td align="left" valign="top">

                    11/26/2008


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >1</td>
                    <td align="left" valign="top" >$75.00</td>
                    <td align="left" valign="top" >$4,476.18</td>
                    <td align="left" valign="top" >$6,883.50 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Wilcox, Vern';
                    					document.getElementById('ids').value='263';
                    					sub();
                    					">
                    Wilcox, Vern
                    </a>

                    </td>
                    <td align="left" valign="top">Wilcox for Council District 4</td>

                    <td align="left" valign="top">

                    07/20/1993


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >4</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$136.39 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Williams, Raeisha';
                    					document.getElementById('ids').value='890';
                    					sub();
                    					">
                    Williams, Raeisha
                    </a>

                    </td>
                    <td align="left" valign="top">Raeisha Williams for Minneapolis  City Council Ward 5</td>

                    <td align="left" valign="top">

                    09/08/2016


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$4,392.50</td>
                    <td align="left" valign="top" >$913.42</td>
                    <td align="left" valign="top" >$5,893.97 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Wilson, David';
                    					document.getElementById('ids').value='970';
                    					sub();
                    					">
                    Wilson, David
                    </a>

                    </td>
                    <td align="left" valign="top">David John Wilson for Magical Thinking</td>

                    <td align="left" valign="top">

                    08/28/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Winstead, Gene';
                    					document.getElementById('ids').value='69';
                    					sub();
                    					">
                    Winstead, Gene
                    </a>

                    </td>
                    <td align="left" valign="top">Winstead for Mayor</td>

                    <td align="left" valign="top">

                    04/02/1999


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Mayor</td>
                    <td align="left" valign="top" ></td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$2,318.04 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Woodruff, Susan';
                    					document.getElementById('ids').value='956';
                    					sub();
                    					">
                    Woodruff, Susan
                    </a>

                    </td>
                    <td align="left" valign="top">Susan &quot;Hofmeister&quot; Woodruff</td>

                    <td align="left" valign="top">

                    07/17/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Bloomington</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$528.00</td>
                    <td align="left" valign="top" >$519.25</td>
                    <td align="left" valign="top" >$8.75 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Yang, Blong';
                    					document.getElementById('ids').value='765';
                    					sub();
                    					">
                    Yang, Blong
                    </a>

                    </td>
                    <td align="left" valign="top">Yang for City Council Campaign Committee</td>

                    <td align="left" valign="top">

                    02/28/2013


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >5</td>
                    <td align="left" valign="top" >$27,072.64</td>
                    <td align="left" valign="top" >$15,895.49</td>
                    <td align="left" valign="top" >$34,959.97 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Young, Annie';
                    					document.getElementById('ids').value='176';
                    					sub();
                    					">
                    Young, Annie
                    </a>

                    </td>
                    <td align="left" valign="top">Young for Parks</td>

                    <td align="left" valign="top">

                    02/28/2001


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >At large</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$13.99 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Yusuf, Fadumo';
                    					document.getElementById('ids').value='927';
                    					sub();
                    					">
                    Yusuf, Fadumo
                    </a>

                    </td>
                    <td align="left" valign="top">Fadumo&#39;s Campaign Voice of Ward 6</td>

                    <td align="left" valign="top">

                    03/01/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$3,786.04</td>
                    <td align="left" valign="top" >$3,786.04</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Zea-Aida, Teqen';
                    					document.getElementById('ids').value='962';
                    					sub();
                    					">
                    Zea-Aida, Teqen
                    </a>

                    </td>
                    <td align="left" valign="top">People of Minneapolis for Teqen</td>

                    <td align="left" valign="top">

                    08/10/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Council Member</td>
                    <td align="left" valign="top" >7</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



                  <tr>
                    <td align="left" valign="top" >
                    <a href="#" onclick="
                    					document.getElementById('fullname').value='Zielinski, Jennifer';
                    					document.getElementById('ids').value='972';
                    					sub();
                    					">
                    Zielinski, Jennifer
                    </a>

                    </td>
                    <td align="left" valign="top">Jennifer Zielinski for Park Board District 6</td>

                    <td align="left" valign="top">

                    08/29/2017


                    </td>
    				<td align="left" valign="top">



                    </td>


                    <td align="left" valign="top" >Minneapolis</td>
                    <td align="left" valign="top" >Park Board</td>
                    <td align="left" valign="top" >6</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00</td>
                    <td align="left" valign="top" >$0.00 </td>

                  </tr>



    			</tbody>
                </table>

                </div>

                <table id='pager' border='0' cellspacing='1' cellpadding='1'>
    <TR><TD class="" colspan=4><CENTER>Records 1 - 181 of 181</CENTER></TD></TR>
    <TR><TD class="" colspan=4>&nbsp;</TD></TR>
    </TABLE>



                <br />




                 <button
    		         type="button"
    	             class="btn btn-primary"
    	             onclick="delete_cookie('saveCommitteSort.bs.table.sortOrder');delete_cookie('saveCommitteSort.bs.table.sortName');document.location.href='search_options.do';">
                 	<span class="glyphicon glyphicon-repeat" aria-hidden="true"></span> Search again
                 </button>
                  <!-- button type="button" class="btn btn-primary" onclick="javascript:sub();">
                  <span class="glyphicon glyphicon-file" aria-hidden="true"></span>

                  View details</button-->

    <input type="hidden" name="searchBy" value="candidate">
    <input type="hidden" name="fullname" id="fullname">
    <input type="hidden" name="ids" id="ids">
    <input type="hidden" name="alpha" value="">

    <input type="hidden" name="city" value="">
    <input type="hidden" name="office" value="">
    <input type="hidden" name="district" value="">
    <input type="hidden" name="filterBy" value="active">

    <input type="hidden" id="ps" name="ps" value="181">

    </form>

    <script>

     $(document).ready(function () {



         var sw = 1;
         $('button[name="toggle"]').attr('title','Summary view');
         $('button[name="toggle"]').appendTo('#nav_panel');

         $('button[name="toggle"]').click(function(){
           if(sw ==1){
    		$('button[name="toggle"]').attr('title','List view');
    		sw=2;
            }else{
            $('button[name="toggle"]').attr('title','Summary view');
            sw=1;
            }


         })

     });
     </script>
    				    </div>
    						</div>
    							</section>

     <aside class="module tert-lvl-sidebar">
            <h5 class="heading-module">Related Pages</h5>
            <ul>
                <li><a href="http://www.hennepin.us/residents/elections/campaign-finance">Campaign finance information </a></li>
                <li><a href="http://www.hennepin.us/residents/elections/file-for-office">File for office </a></li>
                <li><a href="http://www.hennepin.us/residents/elections/campaign-finance#campaign-contrib-limits">Contribution limits</a></li>
                <li><a href="http://www.hennepin.us/residents/elections/campaign-finance#campaign-finance-due-date">Report due dates</a></li>
                <li><a href="http://www.hennepin.us/residents/elections/campaign-finance#campaign-finance-overview ">Reporting overview</a></li>
            </ul>
        </aside>



    	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    	</div>
    	<!-- footer.jsp start -->




    <footer class="site-footer">
    	<h1 class="site-footer__heading desktop">Hennepin County, Minnesota</h1>
    	<ul class="site-footer__social-links">
    		<li><a class="social-icon icon-facebook" href="https://www.facebook.com/hennepin" target="_blank"><span	class="visuallyhidden">Facebook</span></a></li>
    		<li><a class="social-icon icon-twitter" href="https://twitter.com/Hennepin" target="_blank"><span class="visuallyhidden">Twitter</span></a></li>
    		<li><a class="social-icon icon-youtube"	href="http://www.youtube.com/user/HennepinMN" target="_blank"><span	class="visuallyhidden">YouTube</span></a></li>
    		<li><a class="social-icon icon-linkedin" href="http://www.linkedin.com/company/hennepin-county" target="_blank"><span class="visuallyhidden">LinkedIn</span></a></li>
    	</ul>
    	<p class="site-footer__site-legal"><a href="http://www.hennepin.us/your-government/open-government/accessibility-privacy-security.aspx">Privacy</a>|&nbsp; &nbsp;Copyright <script>document.write(new Date().getFullYear());</script></p>
    </footer>
    <a class="top-reminder icon-btn-top-arrow" href="#">Top</a>


    <script>window.jQuery || document.write('<script src="/cfrs/assets/js/vendor/jquery-1.11.3.min.js"><\/script>')</script>
    <script src="/cfrs/assets/js/plugins.js"></script>
    <script src="/cfrs/assets/js/main.js"></script>


    <script>

      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-75832919-1', 'auto');
      ga('send', 'pageview');

    </script>

    <!-- footer.jsp end -->

     </body>
    </html>
    '''
