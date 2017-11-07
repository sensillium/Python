from azure.storage.blob import BlobService

source_account = BlobService(account_name='cngssd', account_key='DVvOtpOVW71er9ztR3mooJk4Zc3ZNovW9YV3qu4Y6bkN0eCfHutpcNVXW6gtpfolRk4CcAlmftz/+SDwm2BQag==')
dest_account = BlobService(account_name='testcng', account_key='piWr6zleZ1sL8aopv5Y4NRYyrVWaW2/QrXcPpsxRec4IxtEoR1IyRmZCkbdyq50Bfu0qidF8SicQahdM+OExvg==')

# list blobs
source_blobs = []
source_marker = None
while True:
    batch = source_account.list_blobs('vhds', marker=source_marker)
    source_blobs.extend(batch)
    if not batch.next_marker:
        break
    source_marker = batch.next_marker
for blob in source_blobs:
    print(blob.name)

dest_blobs = []
dest_marker = None
while True:
    batch = dest_account.list_blobs('vhds', marker=dest_marker)
    dest_blobs.extend(batch)
    if not batch.next_marker:
        break
    dest_marker = batch.next_marker
for blob in dest_blobs:
    print(blob.name)
