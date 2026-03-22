import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): click.echo('SilverStripe serve')
@cli.command()
def dev(): click.echo('SilverStripe dev/build')
if __name__ == '__main__': cli()
