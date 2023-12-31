CREATE TABLE [dbo].[mpi](
	[mpi_id] [int] NOT NULL,
	[created_by] [varchar](60) NOT NULL,
	[created_date] [datetime] NOT NULL,
	[revision_by] [varchar](60) NULL,
	[revision_date] [datetime] NULL,
	[deleted] [varchar](1) NULL,
	[deleted_by] [varchar](60) NULL,
	[deleted_date] [datetime] NULL,
	[title] [varchar](15) NULL,
	[first_name] [varchar](50) NULL,
	[last_name] [varchar](50) NULL,
	[middle_name] [varchar](35) NULL,
	[maiden_name] [varchar](50) NULL,
	[date_of_birth] [datetime] NULL,
	[place_of_birth] [varchar](35) NULL,
	[marital_status_id] [int] NULL,
	[sex] [char](1) NULL,
	[address1] [varchar](35) NULL,
	[address2] [varchar](35) NULL,
	[address3] [varchar](35) NULL,
	[city] [varchar](50) NULL,
	[county_id] [int] NULL,
	[prov_state] [varchar](3) NULL,
	[postal_zip_code] [varchar](15) NULL,
	[country_id] [int] NULL,
	[deceased_date] [datetime] NULL,
	[religion_id] [int] NULL,
	[race_id] [int] NULL,
	[primary_lang_id] [int] NULL,
	[secondary_lang_id] [int] NULL,
	[citizenship_id] [int] NULL,
	[height] [float] NULL,
	[ibw_range] [varchar](50) NULL,
	[veteran_number] [varchar](20) NULL,
	[public_trustee_number] [varchar](20) NULL,
	[education_id] [int] NULL,
	[occupations] [varchar](50) NULL,
	[phone_home] [varchar](35) NULL,
	[phone_cell] [varchar](35) NULL,
	[phone_office] [varchar](35) NULL,
	[phone_office_ext] [varchar](15) NULL,
	[fax] [varchar](35) NULL,
	[phone_pager] [varchar](35) NULL,
	[phone_other] [varchar](35) NULL,
	[email_address] [varchar](75) NULL,
	[web_address] [varchar](75) NULL,
	[ssn_sin] [varchar](30) NULL,
	[suffix] [int] NULL,
	[high_risk] [char](1) NULL,
	[do_not_merge] [char](1) NOT NULL,
	[medicare] [varchar](30) NULL,
	[ssn_required_flag] [bit] NOT NULL,
	[drop_col_moved_to_clients_attribute] [varchar](1000) NULL,
	[HRN_Padding] [char](1) NOT NULL,
	[ethnicity_id] [int] NULL,
	[mbi] [varchar](30) NULL,
	[sexual_orientation_id] [int] NULL,
	[sexual_orientation_other] [varchar](32) NULL,
	[gender_identity_id] [int] NULL,
	[gender_identity_other] [varchar](32) NULL,
	[preferred_name] [varchar](50) NULL,
	[phone_home_ext] [varchar](15) NULL,
	[phone_cell_ext] [varchar](15) NULL,
	[fax_ext] [varchar](15) NULL,
	[phone_pager_ext] [varchar](15) NULL,
	[phone_other_ext] [varchar](15) NULL,
	[preferred_contact_point] [varchar](16) NULL
)