Polygon and Soil Data Collection – Agro API Integration
Project Goal
This script was developed to collect soil information for mapped agricultural plots (polygons) using the Agromonitoring API. It retrieves polygon data (such as location IDs) and uses them to request detailed soil characteristics. The results are saved in a structured CSV file for further analysis or integration into geospatial, agricultural, or environmental datasets.
Workflow Summary
1. Connecting to the Agro API
The script first connects to the Agromonitoring Polygon API, which returns a list of pre-registered polygon areas (e.g., farm boundaries or plots). Each polygon includes a unique ID, which is needed to request further details. Authentication is handled via an API key.

2. Fetching Soil Data
A function fetch_poly_id(id) is defined to retrieve soil data for a given polygon. It connects to the Agromonitoring Soil API, passing both the API key and the polygon ID. The response includes soil attributes such as:
	dt – Timestamp: This field represents the date and time when the soil data was recorded or collected. Format: Usually in UNIX timestamp format (e.g., 1719052800) or ISO format (e.g., 2025-06-22T03:00:00Z). Purpose: Helps track when each soil measurement was taken, enabling trend analysis or time-based comparisons.

	t10 – Temperature at 10 cm Depth: This represents the soil temperature measured at 10 centimetres below the surface. Unit: Degrees Celsius (°C), Crucial for understanding root-zone temperature, which affects seed germination, root growth, and microbial activity.

	moisture – Soil Moisture Content: The amount of water present in the soil, typically measured as volumetric water content. Unit: Cubic meters of water per cubic meter of soil (m³/m³) or sometimes as a percentage. Essential for assessing irrigation needs, drought conditions, or soil health. A key metric in precision agriculture.

	t0 – Surface Temperature: This indicates the temperature at the surface level of the soil (0 cm depth). Unit: Degrees Celsius (°C), Useful for evaluating evaporation rates, heat stress, or surface-level environmental interactions.

3. User-Defined Data Collection
The script prompts the user to input the number of polygon records to process. It then loops through that number of polygon IDs and fetches soil data for each.

4. Writing to CSV
The soil data for each polygon is saved in a file called polygon_data.csv. The first record is used to extract and define the CSV headers. Each subsequent record is added as a new row in the file. A preview of each result is printed to the console (optional for monitoring progress). Each row in the resulting CSV file represents soil data for a different polygon. Example fields include:


dt – Timestamp	t10 – Temperature at 10 cm Depth	Moisture – Soil Moisture Content	t0 – Surface Temperature
1750550400	298.935	0.285	293.812

Business & Analytical Value
	Soil Health Monitoring: Enables teams to collect and analyse soil quality indicators at the polygon (plot) level. 
	Precision Agriculture: Supports tailored decisions for fertilizer application, crop planning, and irrigation.
	Data Integration: Output can be joined with farm location maps, yield data, or climate models for deeper insights.
	User-Controlled Fetching: Allowing users to decide how many records to pull adds flexibility, especially during testing or incremental data collection.
	Implementation Notes
	API Key Security: The API key is hard-coded. In production, consider storing it securely in environment variables or a configuration file.
	No Retry/Error Recovery: There is no handling for API limits, timeouts, or malformed responses. These should be addressed if scaled for broader use.
	Polygon Registration: This script assumes polygons have already been created in the Agromonitoring system. If not, an additional step to register them would be needed.

Summary
This script retrieves polygon-based soil data from the Agromonitoring API and stores it in a structured CSV file. It helps lay the groundwork for data-driven agricultural analysis, supporting smarter planning and field management through accessible environmental data.
It is modular and can be extended to: Work with multiple users or locations Connect to a live dashboard or alert system Be integrated with other remote sensing data or weather feeds
Link to script

