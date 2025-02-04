"""Initial data required for core sites."""
from nautobot.apps.jobs import register_jobs

from nautobot_design_builder.design_job import DesignJob
from nautobot.dcim.models import Location
from nautobot.extras.jobs import ObjectVar, StringVar, IPNetworkVar

from .context import SpineLeafDesignContext


class SpineLeafDesign(DesignJob):
    """Initialize the database with default values needed by the core site designs."""
    
    region = ObjectVar(
        label="Region",
        description="Region for the new backbone site",
        model=Location,
    )

    site_name = StringVar(regex=r"\w{3}\d+")

    site_prefix = IPNetworkVar(min_prefix_length=16, max_prefix_length=24)

    class Meta:
        """Metadata needed to implement the backbone site design."""

        name = "Spine-Leaf Design"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = SpineLeafDesignContext

name = "Demo Designs"
register_jobs(SpineLeafDesign)
