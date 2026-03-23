import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('akamai_cli running')
@cli.command()
def start(): click.echo('akamai_cli started')
if __name__ == '__main__': cli()
