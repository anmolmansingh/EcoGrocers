from firebase import db
from app.models import Product

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        data = doc.to_dict()
        Product.objects.update_or_create(
            id=doc.id,
            defaults={
                'name': data['name'],
                'price': data['price'],
                'quantity': data['quantity']
            }
        )

doc_ref = db.collection('products')
doc_watch = doc_ref.on_snapshot(on_snapshot)
