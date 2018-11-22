App hosted on Heroku at https://sendit299.herokuapp.com/api/v1/          
<br/>
User interface hosted at https://nyabongoedgar.github.io/SendIT/UI/
<br/>
[![Build Status](https://travis-ci.org/nyabongoedgar/SendIT.svg?branch=ft-challenge-three)](https://travis-ci.org/nyabongoedgar/SendIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/de8d6ff5a0fdf45eba8c/maintainability)](https://codeclimate.com/github/nyabongoedgar/SendIT/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/nyabongoedgar/SendIT/badge.svg?branch=ft-challenge-three)](https://coveralls.io/github/nyabongoedgar/SendIT?branch=ft-challenge-three)

<h1> Working Endpoints</h1>
<p><em>Before using the routes below, you should first signup and then login, After your session, you <b>must</b> logout by using the logout route</em></p>
<p>To signup, visit, https://sendinc.herokuapp.com/api/v1/signup and provide a "username", "password" and "email", all must be a string</p>
<p>To signin, visit, https://sendinc.herokuapp.com/api/v1/login and provide the "username" and the "password" you used to create the account.</p>
<p>To logout, visit, https://sendinc.herokuapp.com/api/v1/logout with a get method</p>

<ol>
<li>GET /parcels, accessible at https://sendit299.herokuapp.com/api/v1/parcels </li>
<li>GET /users/userId/parcels, accessible at https://sendit299.herokuapp.com/api/v2/users/userId/parcels </li>
<li>PUT /parcels/parcelId/destination accessible at https://sendit299.herokuapp.com/api/v2/users/userId/parcels </li>
<li>PUT /parcels/parcelId/cancel, accessible at https://sendinc.herokuapp.com/api/v2/parcels/parcelId/cancel </li>

<li>POST /parcels, accessible at https://sendinc.herokuapp.com/api/v1/parcels 
<br> A parcel order should look like this <br> 
{'parcel_description':'this parcel contains a phone',
'parcel_weight':50,
'parcel_source':'Ntinda',
'parcel_destination':'Mbarara',
'receiver_name':'Ritah',
'receiver_telephone':'077890340',
'current_location':'Ntinda',
'status':'pending'}</li>
</ol>
<h2> Getting Started </h2>
<h2> Pre-requisites </h2>

<ul><li>Python 3.5 https://www.python.org/getit/</li>
<li>pip https://pip.pypa.io/en/stable/installing/</li>
<li>Flask 1.0.2, install, pip install Flask </li></ul>
  

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

