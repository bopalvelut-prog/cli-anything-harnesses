import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deploy(): subprocess.run(['fly', 'deploy'])
@cli.command()
def status(): subprocess.run(['fly', 'status'])
@cli.command()
def logs(): subprocess.run(['fly', 'logs'])
@cli.command()
def ssh(): subprocess.run(['fly', 'ssh', 'console'])
if __name__ == '__main__': cli()
