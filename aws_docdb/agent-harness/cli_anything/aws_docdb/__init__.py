import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_docdb running')
@cli.command()
def start(): click.echo('aws_docdb started')
if __name__ == '__main__': cli()
