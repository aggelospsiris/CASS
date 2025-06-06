_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_context60.txt',
    prob_thd=0.1,

    # CLIPb16 DINOb8
    global_semantics_weight = 0.25,
    mean_vector_weight = 0.04,
    h_threshold = 0.09

)

# dataset settings
dataset_type = 'PascalContext60Dataset'
data_root = ''

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(2048, 336), keep_ratio=True),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='JPEGImages', seg_map_path='SegmentationClassContext'),
        ann_file='ImageSets/SegmentationContext/val.txt',
        pipeline=test_pipeline))
