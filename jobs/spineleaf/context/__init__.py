from nautobot_design_builder.context import Context, context_file


@context_file("context.yaml")
class SpineLeafDesignContext(Context):
    """Render context for SpineLeaf design"""
