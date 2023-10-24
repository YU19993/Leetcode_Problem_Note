def compareVersion(version1: str, version2: str) -> int:
    # Split the versions by '.' to get the revisions
    v1_revisions = version1.split('.')
    v2_revisions = version2.split('.')
    
    # Get the maximum number of revisions between the two versions
    max_length = max(len(v1_revisions), len(v2_revisions))
    
    for i in range(max_length):
        # Get the revision at the current index for both versions. If a revision doesn't exist, treat it as 0
        v1_revision = int(v1_revisions[i]) if i < len(v1_revisions) else 0
        v2_revision = int(v2_revisions[i]) if i < len(v2_revisions) else 0
        
        # Compare the revisions
        if v1_revision > v2_revision:
            return 1
        elif v1_revision < v2_revision:
            return -1

    # If we reach here, the versions are equal
    return 0
