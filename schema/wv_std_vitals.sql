CREATE TABLE [dbo].[wv_std_vitals](
	[std_vitals_id] [int] NOT NULL,
	[fac_id] [int] NOT NULL,
	[description] [varchar](20) NOT NULL,
	[sequence_no] [int] NULL,
	[short_description] [char](10) NULL,
	[valid_eom] [char](1) NULL,
	[min_value] [decimal](6, 2) NULL,
	[max_value] [decimal](6, 2) NULL
)