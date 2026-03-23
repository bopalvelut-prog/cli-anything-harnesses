import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cssnano running')
@cli.command()
def start(): click.echo('cssnano started')
if __name__ == '__main__': cli()
