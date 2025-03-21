# NEPSE Extract

The following script extacts data from Datewise Idices depending upon the value passed - NEPSE, Sensitive, Float, Banking, Hotels indices are extracted.

The page uses POST method to pass the variable topTenBased from the select object and then same page loads the data accordingly. I hadn't pulled the data from page using POST before.

Here is the source code and the value of different options in *Indices.php*
```
	<option value="58">NEPSE</option>
	<option value="57">Sensitive</option>
	<option value="62">Float</option>
	<option value="63">Sen. Float</option>
	<option value="51">Banking</option>
	<option value="61">Trading</option>
	<option value="52">Hotels</option>
	<option value="55">Dev. Bank</option>
	<option value="54">HydroPower</option>
	<option value="60">Finance</option>
	<option value="59">Insurance</option>
	<option value="56">Manu.& Pro.</option>
	<option value="53">Others</option>
```

Pick the corresponding value to extract the data from the available options

```python
postdata= {  
    'topTenBased' : '58', #value from Select menu (NEPSE) 
    'Submit' : 'Submit'
    }
```
[http://rvibek.com.np/extract-nepse-data/](https://rvibek.com.np/extract-nepse-data.html)
