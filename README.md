App hosted on Heroku at https://sendinc.herokuapp.com/api/v1/
User interface hosted at https://nyabongoedgar.github.io/SendIT/UI/
<br>
[![Coverage Status](https://coveralls.io/repos/github/nyabongoedgar/SendIT/badge.svg?branch=ft-challenge-two)](https://coveralls.io/github/nyabongoedgar/SendIT?branch=ft-challenge-two)
[![Build Status](https://travis-ci.org/nyabongoedgar/SendIT.svg?branch=ft-challenge-two)](https://travis-ci.org/nyabongoedgar/SendIT)<a href="https://codeclimate.com/github/nyabongoedgar/SendIT/maintainability"><img src="https://api.codeclimate.com/v1/badges/de8d6ff5a0fdf45eba8c/maintainability" /></a>

<h1> Getting Started </h1>
<h2> Pre-requisites </h2>

<ul><li>Python 3.5 https://www.python.org/getit/</li><li>pip https://pip.pypa.io/en/stable/installing/</li><li>Flask 1.0.2</li></ul>
  

<h2>Preparing development environment</h2>
<ul><li>Make a directory named Store-Manager<br>
  $ mkdir SendIT <br>
  $ cd ~/SendIT
  </li>

<li> Set up a virtual environment: on windows <br>
    $ python -m virtualenv venv <br>
    $ venv/Scripts/activate </li>
  
<li>Clone git repository <br>
  $ git clone https://github.com/nyabongoedgar/SendIT.git</li>
<li>Switch to "ft-challenge-two" branch</li>
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

</table>  