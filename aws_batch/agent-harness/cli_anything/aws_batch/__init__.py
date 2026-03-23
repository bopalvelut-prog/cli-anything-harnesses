import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_batch running')
@cli.command()
def start(): click.echo('aws_batch started')
if __name__ == '__main__': cli()
