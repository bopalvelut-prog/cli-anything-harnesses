import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def canister(): click.echo('IC canister')
@cli.command()
def deploy(): click.echo('IC deploy')
if __name__ == '__main__': cli()
