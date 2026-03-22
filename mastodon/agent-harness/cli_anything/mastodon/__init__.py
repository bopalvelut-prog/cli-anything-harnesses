import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def toot(): click.echo('Mastodon toot')
@cli.command()
def timeline(): click.echo('Mastodon timeline')
if __name__ == '__main__': cli()
