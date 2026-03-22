import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def capture(): subprocess.run(['sysdig', '-w', 'capture.scap'])
@cli.command()
def chisel(): subprocess.run(['sysdig', '-cl'])
if __name__ == '__main__': cli()
