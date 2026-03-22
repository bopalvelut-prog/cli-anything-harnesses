import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Trezor status')
@cli.command()
def accounts(): click.echo('Trezor accounts')
if __name__ == '__main__': cli()
