from __future__ import annotations

from html import escape

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.hooks import hooks
from src.database.models.plugin import InstalledPlugin

PLUGIN_NAME = "plg_robots_meta"


def setup(registry: object) -> None:
    hooks.on("frontend.head", render_head)


async def _settings(db: AsyncSession | None) -> dict[str, object]:
    if db is None:
        return {}
    plugin = (
        await db.execute(select(InstalledPlugin).where(InstalledPlugin.name == PLUGIN_NAME))
    ).scalar_one_or_none()
    return plugin.settings if plugin and isinstance(plugin.settings, dict) else {}


async def render_head(
    *,
    db: AsyncSession | None = None,
    **kwargs: object,
) -> str:
    settings = await _settings(db)
    robots = str(settings.get("robots") or "").strip()
    if not robots:
        return ""
    return f'<meta name="robots" content="{escape(robots, quote=True)}">'
