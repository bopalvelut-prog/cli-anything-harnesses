import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_data_exchange running')
@cli.command()
def start(): click.echo('aws_data_exchange started')
if __name__ == '__main__': cli()
