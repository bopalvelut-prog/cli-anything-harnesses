import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def fabric(): click.echo('Hyperledger Fabric')
@cli.command()
def explorer(): click.echo('Blockchain Explorer')
if __name__ == '__main__': cli()
