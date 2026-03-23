import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('construct running')
@cli.command()
def start(): click.echo('construct started')
if __name__ == '__main__': cli()
