import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def mint(): click.echo('NFTPort mint')
@cli.command()
def deploy(): click.echo('NFTPort deploy')
if __name__ == '__main__': cli()
