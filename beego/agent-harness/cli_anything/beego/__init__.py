import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beego running')
@cli.command()
def start(): click.echo('beego started')
if __name__ == '__main__': cli()
