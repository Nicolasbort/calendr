from drf_spectacular.utils import OpenApiExample

EXAMPLES_READ_MANY = [
    OpenApiExample(
        name="List of notification IDs",
        description="Only not read notifications will be updated.",
        value=[
            "949a95ac-9724-4670-8da9-2f59656942a2",
            "dbb10a2e-c27a-46cb-b6d7-fafed7dfb75a",
            "0811a334-8532-463c-a2b5-2b68f32e463e",
        ],
    )
]
