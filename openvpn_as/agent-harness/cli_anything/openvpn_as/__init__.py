import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OpenVPN AS running')
@cli.command()
def login(): click.echo('Login to OpenVPN AS')
if __name__ == '__main__': cli()
