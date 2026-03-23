import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pagoda running')
@cli.command()
def start(): click.echo('pagoda started')
if __name__ == '__main__': cli()
