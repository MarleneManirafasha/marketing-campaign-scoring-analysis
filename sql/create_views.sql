CREATE VIEW vw_campaign_performance AS
SELECT 
    COUNT(*) as total_clients,
    SUM(response_flag) as total_responders,
    ROUND(AVG(response_flag::numeric)*100,2) as response_rate
FROM campaign_data;


CREATE VIEW vw_scoring_segments AS
SELECT *,
CASE
    WHEN score > 0.7 THEN 'High Potential'
    WHEN score > 0.4 THEN 'Medium Potential'
    ELSE 'Low Potential'
END as segment
FROM campaign_data;