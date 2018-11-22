<<<<<<< HEAD
App hosted on Heroku at https://sendinc.herokuapp.com/api/v1/   
User interface hosted at https://nyabongoedgar.github.io/SendIT/UI/
<br>
[![Coverage Status](https://coveralls.io/repos/github/nyabongoedgar/SendIT/badge.svg?branch=ft-challenge-two)](https://coveralls.io/github/nyabongoedgar/SendIT?branch=ft-challenge-two)
[![Build Status](https://travis-ci.org/nyabongoedgar/SendIT.svg?branch=ft-challenge-two)](https://travis-ci.org/nyabongoedgar/SendIT)<a href="https://codeclimate.com/github/nyabongoedgar/SendIT/maintainability"><img src="https://api.codeclimate.com/v1/badges/de8d6ff5a0fdf45eba8c/maintainability" /></a>
<h1> Getting Started </h1>
<h2> Pre-requisites </h2>

<ul><li>Python 3.5 https://www.python.org/getit/</li><li>pip https://pip.pypa.io/en/stable/installing/</li><li>Flask 1.0.2</li></ul>
=======
App hosted on Heroku at https://sendit299.herokuapp.com/api/v2/          
<br/>
User interface hosted at https://nyabongoedgar.github.io/SendIT/UI/
<br/>
[![Build Status](https://travis-ci.org/nyabongoedgar/SendIT.svg?branch=ft-challenge-three)](https://travis-ci.org/nyabongoedgar/SendIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/de8d6ff5a0fdf45eba8c/maintainability)](https://codeclimate.com/github/nyabongoedgar/SendIT/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/nyabongoedgar/SendIT/badge.svg?branch=ft-challenge-three)](https://coveralls.io/github/nyabongoedgar/SendIT?branch=ft-challenge-three)

<h1> Working Endpoints</h1>
<p><em>Before using the routes below, you should first signup and then login, After your session, you <b>must</b> logout by using the logout route</em></p>
<p>To signup, visit, https://sendinc.herokuapp.com/api/v2/signup and provide a "username", "password" and "email", all must be a string</p>
<p>To signin, visit, https://sendinc.herokuapp.com/api/v2/login and provide the "username" and the "password" you used to create the account.</p>
<p>To logout, visit, https://sendinc.herokuapp.com/api/v2/logout with a get method</p>

<ol>
<li>POST /auth/signup, accesible at https://sendit299.herokuapp.com/api/v2/auth/signup</li>
<li>POST /auth/login, accesible at https://sendit299.herokuapp.com/api/v2/auth/login</li>

<li>POST /parcels, accessible at https://sendinc.herokuapp.com/api/v2/parcels 
<br> A parcel order should look like this <br> 
{'parcel_description':'this parcel contains a phone',
'parcel_weight':50,
'parcel_source':'Ntinda',
'parcel_destination':'Mbarara',
'receiver_name':'Ritah',
'receiver_telephone':'077890340',
'current_location':'Ntinda',
'status':'pending'}</li>
<li>GET /parcels, accessible at https://sendit299.herokuapp.com/api/v2/parcels </li>
<li>PUT /parcels/parcelId/destination accessible at https://sendit299.herokuapp.com/api/v2/parcels/parcelId/destination </li>
<li>PUT /parcels/parcelId/status, accessible at https://sendit299.herokuapp.com/api/v2/parcels/parcelId/status </li>
<li>PUT /parcels/parcelId/presentLocation , accessible at https://sendit299.herokuapp.com/api/v2//parcels/parcelId/presentLocation</li>
</ol>
<h2> Getting Started </h2>
<h2> Pre-requisites </h2>

<ul><li>Python 3.5 https://www.python.org/getit/</li>
<li>pip https://pip.pypa.io/en/stable/installing/</li>
<li>Flask 1.0.2, install, pip install Flask </li></ul>
>>>>>>> feedback-two
  

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
<<<<<<< HEAD
<li>Switch to "ft-challenge-two" branch</li>
=======
<li>Switch to "develop" branch</li>
>>>>>>> feedback-two
  <li>Install necessary requirements<br>
  $ pip install -r requirements.txt </li>
<li>Run the main app file <br>
  $ python run.py
 </li> </ul>
  
<<<<<<< HEAD
<b>This site runs at http://127.0.0.1:5000/api/v1/</b> 
=======
<b>This site runs at http://127.0.0.1:5000/api/v2/</b> 
>>>>>>> feedback-two
  
  
<h2>Project Overview </h2>

<p>SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.</p>

 <hr/>
<p> This applcation contains a set of API endpoints already defined below and use data structures to store data in memory </p>


<caption>API endpoints</caption>
<table>
<tr><td>EndPoint</td>	<td>Functionality</td>	</tr>

<<<<<<< HEAD
<tr><td>GET /parcels</td>	<td>Fetch all parcel delivery orders</td>	</tr>

<tr><td>GET /parcels/<parcelId></td>	<td>Fetch a specific parcel delivery order</td>	</tr>

<tr><td>GET /users/<userId>/parcels	</td> <td>Fetch all parcel delivery orders by a specific user</td>	</tr>

<tr><td>PUT /parcels/<parcelId>/cancel</td>	<td>Cancel the specific parcel delivery order</td>	</tr>

<tr><td>POST /parcels</td>	<td>Create a parcel delivery order</td>	</tr>

</table>  
=======
<tr><td>POST /auth/signup</td>	<td>Register a user</td>	</tr>

<tr><td>POST /auth/login	</td> <td>Login a user</td>	</tr>

<tr><td>PUT /parcels/parcelId/destination</td>	<td>Change the location of a specific parcel delivery order</td>	</tr>

<tr><td>GET admin/parcels</td>	<td>Fetch all parcel delivery order</td>	</tr>

<tr><td>PUT /parcels/parcelId/status</td>	<td>Change the status of a specific parcel delivery order</td>	</tr>

tr><td>PUT /parcels/parcelId/presentLocation</td>	<td>Change the present location of a specific parcel delivery order</td>	</tr>

<tr><td>GET /parcels</td>	<td>Fetch all parcel delivery orders</td>	</tr>

<tr><td>GET admin/parcels</td>	<td>Fetch all parcel delivery order</td>	</tr>

</table>

>>>>>>> feedback-two
