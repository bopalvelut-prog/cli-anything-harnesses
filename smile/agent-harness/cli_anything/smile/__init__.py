import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smile running')
@cli.command()
def start(): click.echo('smile started')
if __name__ == '__main__': cli()
