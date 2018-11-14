App hosted on Heroku at https://sendinc.herokuapp.com/api/v1/          
<br/>
User interface hosted at https://nyabongoedgar.github.io/SendIT/UI/
<br/>

[![Build Status](https://travis-ci.org/nyabongoedgar/SendIT.svg?branch=develop)](https://travis-ci.org/nyabongoedgar/SendIT)<a href="https://codeclimate.com/github/nyabongoedgar/SendIT/maintainability"><img src="https://api.codeclimate.com/v1/badges/de8d6ff5a0fdf45eba8c/maintainability" /></a>
[![Coverage Status](https://coveralls.io/repos/github/nyabongoedgar/SendIT/badge.svg?branch=develop)](https://coveralls.io/github/nyabongoedgar/SendIT?branch=develop)

<h1> Working Endpoints</h1>
<p><em>Before using the routes before, you should first signup and then login, After your session, you can logout by using the logout route</em></p>
<p>To signup, visit, https://sendinc.herokuapp.com/api/v1/signup and provide a "username", "password" and "email", all must be a string</p>
<p>To signin, visit, https://sendinc.herokuapp.com/api/v1/login and provide the "username" and the "password" you used to create the account.</p>
<p>To logout, visit, https://sendinc.herokuapp.com/api/v1/logout with a get method</p>
<ol>
<li>GET /parcels, accessible at https://sendinc.herokuapp.com/api/v1/parcels </li>
<li>GET /parcels/<parcelId>, accessible at https://sendinc.herokuapp.com/api/v1/parcels/<int:parcelId> </li>
<li>GET /users/<userId>/parcels, accessible at https://sendinc.herokuapp.com/api/v1/users/<int:userId>/parcels </li>
<li>PUT /parcels/<parcelId>/cancel, accessible at https://sendinc.herokuapp.com/api/v1/parcels/<int:parcelId>/cancel </li>
<li>POST /parcels, accessible at https://sendinc.herokuapp.com/api/v1/parcels 
<br> A parcel order should look like this <br> {
        "parcel_name":"bag",
        "parcel_source":"Bukoto",
        "parcel_destination":"Kamwokya",
        "parcel_weight":30,
        "receiver_name":"Chris Tomlin",
        "receiver_telephone":"0779865557"
        }</li>
</ol>
<h2> Getting Started </h2>
<h2> Pre-requisites </h2>

<ul><li>Python 3.5 https://www.python.org/getit/</li><li>pip https://pip.pypa.io/en/stable/installing/</li><li>Flask 1.0.2</li></ul>
  

<h2>Preparing development environment</h2>
<ul><li>Make a directory named SendIT<br>
  $ mkdir SendIT <br>
  $ cd ~/SendIT
  </li>

<li> Set up a virtual environment: on windows <br>
    $ python -m virtualenv venv <br>
    $ venv/Scripts/activate </li>
  
<li>Clone git repository <br>
  $ git clone https://github.com/nyabongoedgar/SendIT.git</li>
<li>Switch to "develop" branch</li>
  <li>Install necessary requirements<br>
  $ pip install -r requirements.txt </li>
<li>Run the main app file <br>
  $ python run.py
 </li> </ul>
  
<b>This site runs at http://127.0.0.1:5000/api/v1/</b> 
  
  
<h2>Project Overview </h2>

<p>SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.</p>

 <hr/>
<p> This applcation contains a set of API endpoints already defined below and use data structures to store data in memory </p>


<caption>API endpoints</caption>
<table>
<tr><td>EndPoint</td>	<td>Functionality</td>	</tr>

<tr><td>GET /parcels</td>	<td>Fetch all parcel delivery orders</td>	</tr>

<tr><td>GET /parcels/<parcelId></td>	<td>Fetch a specific parcel delivery order</td>	</tr>

<tr><td>GET /users/<userId>/parcels	</td> <td>Fetch all parcel delivery orders by a specific user</td>	</tr>

<tr><td>PUT /parcels/<parcelId>/cancel</td>	<td>Cancel the specific parcel delivery order</td>	</tr>

<tr><td>POST /parcels</td>	<td>Create a parcel delivery order</td>	</tr>

