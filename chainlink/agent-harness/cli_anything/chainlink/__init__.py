import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def oracle(): click.echo('Chainlink oracle')
@cli.command()
def vrf(): click.echo('Chainlink VRF')
if __name__ == '__main__': cli()
