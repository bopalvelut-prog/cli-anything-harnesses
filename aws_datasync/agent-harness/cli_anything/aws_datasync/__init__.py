import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_datasync running')
@cli.command()
def start(): click.echo('aws_datasync started')
if __name__ == '__main__': cli()
