## Input Json format

```javascript
{
	"nodes": [
		{
			"name": "cat",
			"id": 2,
			"influence": 5
		}
	],
	"links": [
		{
			"source": 0,
			"target": 1,
			"value": 2
		}
	]
}
```
## notes

"Influence" property is used to determine node's height in style(either obtained from the word frequency from tweet data, or other methods that can determine a node's influence value, and frequency is the most plain naive way to do that), and positive and negative santiment value should sum up to this "influence".

Link's "value" property defines the link width to either "Positive" or "Negative" sentiment. The value linking to these two sentiments should sum up to that node's "influence" property, so that it make more senses visually.

Then by suming all the link "value" up, we can obtain a total "Positive" sum and total "Negative" sum, which can be further normalized to be shown as percentage.

