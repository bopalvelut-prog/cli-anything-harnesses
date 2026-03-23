import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('auditor running')
@cli.command()
def start(): click.echo('auditor started')
if __name__ == '__main__': cli()
