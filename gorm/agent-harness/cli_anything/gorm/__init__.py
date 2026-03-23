import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gorm running')
@cli.command()
def start(): click.echo('gorm started')
if __name__ == '__main__': cli()
