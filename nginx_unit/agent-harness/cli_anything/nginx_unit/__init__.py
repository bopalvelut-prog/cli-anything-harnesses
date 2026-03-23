import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nginx_unit running')
@cli.command()
def start(): click.echo('nginx_unit started')
if __name__ == '__main__': cli()
