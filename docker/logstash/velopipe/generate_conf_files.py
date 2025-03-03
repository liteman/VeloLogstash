# List of strings
strings = [
    "Windows.NTFS.MFT",
    "Windows.Forensics.USN",
    "Windows.Detection.Amcache",
    "Generic.Forensic.SQLiteHunter",
    "Windows.Analysis.EvidenceOfDownload",
    "Windows.Analysis.EvidenceOfExecution",
    "Windows.Applications.TeamViewer.Incoming",
    "Windows.Applications.IISLogs",
    "Windows.Applications.MegaSync",
    "Windows.EventLogs.Evtx",
    "Windows.EventLogs.ExplicitLogon",
    "Windows.EventLogs.PowershellScriptblock",
    "Windows.EventLogs.RDPAuth",
    "Windows.EventLogs.ServiceCreationComspec",
    "Windows.EventLogs.ScheduledTasks",
    "Windows.Forensics.CertUtil",
    "Windows.Forensics.Prefetch",
    "Windows.Forensics.RecycleBin",
    "Windows.Forensics.SRUM",
    "Windows.Forensics.Shellbags",
    "Windows.Forensics.UserAccessLogs",
    "Windows.Network.NetstatEnriched",
    "Windows.Persistence.PowershellProfile",
    "Windows.Registry.MountPoints2",
    "Windows.Registry.PortProxy",
    "Windows.Registry.RDP",
    "Windows.Registry.RecentDocs",
    "Windows.Registry.UserAssist",
    "Windows.Sys.AllUsers",
    "Windows.Sys.Interfaces",
    "Windows.Sys.Programs",
    "Windows.Sys.FirewallRules",
    "Windows.System.Powershell.PSReadline",
    "Windows.System.DNSCache",
    "Windows.System.LocalAdmins",
    "Windows.System.Pslist",
    "Windows.System.TaskScheduler"
]

# Template for the logstash filter
logstash_template = """filter {{
    if "velociraptor" in [tags] {{
        if "{artifact}" in [Artifact] {{
            #customize fields
        }}
    }}
}}"""

# Loop through each string and create a file
for index, string in enumerate(strings, start=102):
    # Format the file name with the index and the string
    file_name = f"{index}-{string.replace('.', '_')}.conf"
    
    # Format the logstash filter with the artifact name
    logstash_filter = logstash_template.format(artifact=string)
    
    # Write the filter to the file
    with open(file_name, 'w') as f:
        f.write(logstash_filter)
        
    print(f"Generated {file_name}")
