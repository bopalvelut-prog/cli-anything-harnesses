import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def publish(): click.echo('WriteFreely publish')
@cli.command()
def posts(): click.echo('WriteFreely posts')
if __name__ == '__main__': cli()
