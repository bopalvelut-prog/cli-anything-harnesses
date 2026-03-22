import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def declare(): click.echo('StarkNet declare')
@cli.command()
def deploy(): click.echo('StarkNet deploy')
if __name__ == '__main__': cli()
