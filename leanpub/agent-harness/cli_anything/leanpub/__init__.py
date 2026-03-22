import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def preview(): click.echo('Leanpub preview')
@cli.command()
def publish(): click.echo('Leanpub publish')
if __name__ == '__main__': cli()
