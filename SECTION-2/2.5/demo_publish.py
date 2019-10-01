<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:bffb6a98a16caaac56871f2acf999d9f03e3e2f06dedf0f69fc7037778565a25
size 259
=======
import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(project_id=os.getenv('PROJECT_ID'), topic=os.getenv('TOPIC_NAME'))

publisher.publish(topic_name, b'Hello World!')
>>>>>>> 1208bfe06536730cf9b4d3020469041d29f05060
