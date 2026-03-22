import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Trust Wallet status')
if __name__ == '__main__': cli()
