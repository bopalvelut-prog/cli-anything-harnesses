import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('siemens running')
@cli.command()
def start(): click.echo('siemens started')
if __name__ == '__main__': cli()
